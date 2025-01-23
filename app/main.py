import sys
import os
import subprocess
import shlex

def main():
    # List of built-in commands
    commands = ['echo', 'exit', 'type', 'pwd', 'cd']
    paths = os.getenv("PATH").split(":")

    while True:
        # Always print the prompt before input
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Ensure prompt is displayed immediately

        # For the final 'command not found' case
        flag = 0
        
        # Wait for user input
        command = input()

        # If the command is not given or NULL, skip that iteration and start the next
        if not command.strip():
            continue

        # Split the command using shlex.split to properly handle quoted arguments
        parts = shlex.split(command)
        
        match parts:
            case ['exit', '0']:
                sys.exit(0)
            case ['echo', *args]:
                # Handle the echo command
                print(' '.join(args))
            case ['cat', *args]:
                # Ensure the arguments are passed correctly to subprocess without extra quotes
                command = ['cat'] + args
                # Execute the command using subprocess and capture the output
                result = subprocess.run(command, capture_output=True, text=True)
                # If successful, print the content from stdout
                if result.returncode == 0:
                    print(result.stdout, end='')
                else:
                    print(f"Error executing cat: {result.stderr}")
            case ['type', arg]:
                if arg in commands:
                    print(f"{arg} is a shell builtin")
                else:
                    for path in paths:
                        if os.path.exists(f"{path}/{arg}"):
                            flag = 1
                            print(f"{arg} is {path}/{arg}")
                            break
                    if flag == 0:
                        print(f"{arg}: not found")
            case ['pwd']:
                # Get current working directory
                print(os.getcwd())
            case ['cd', directory]:
                # Expand user directory and change the path
                directory = os.path.expanduser(directory)
                try:
                    os.chdir(directory)
                except OSError:
                    print(f"cd: {directory}: No such file or directory")
            case [comm, *args]:
                for path in paths:
                    # Saving the execution path of the binary to a variable
                    execpath = f"{path}/{comm}"
                    if os.path.exists(execpath):
                        # Using subprocess instead of os.system to properly give the arguments for the commands
                        result = subprocess.run([comm] + args, executable=execpath)
                        # Flag used here to denote that the command is valid and executed
                        flag = 1
                        break
                if flag == 0:
                    # When the command is not found in our list or the OS binaries
                    print(f"{comm}: command not found")
#added all the changes in quoting
if __name__ == "__main__":
    main()