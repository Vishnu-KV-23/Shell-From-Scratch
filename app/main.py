import sys
import os
import subprocess

def main():
    # Wait for user input
    commands=['echo','exit','type','pwd','cd']
    paths=os.getenv("PATH").split(":")
    while(True):
        #everytime the shell starts this should be printed
        sys.stdout.write("$ ")
        #for the final if case purpose, that is command not founnd
        flag=0
        command=input()
        if not command.strip():
            #if the command is not given or NULL skip that iteration and start the next
            continue
        #the string command is split into list with the spaces and a switch case is later used inorder to check if the preferred command is present in it
        parts=command.split()
        match parts:
            case ['exit','0']:
                sys.exit(0)
            case ['echo',*args]:
                print(' '.join(args))
            case ['type',arg]:
                if arg in commands:
                    print(f"{arg} is a shell builtin")
                else:
                    
                    for path in paths:
                        if os.path.exists(f"{path}/{arg}"):
                            flag=1
                            #"print(f"{arg} is a shell builtin")" print this message only if we have written the implementation 0f the same in our command and it is put in our commands list
                            print(f"{arg} is {path}/{arg}")
                            break
                
                    
                    if (flag==0):
                        print(f"{arg}: not found")
            case ['pwd']:
                #os function to get current working directory
                print(os.getcwd())
            case ['cd',directory]:
                #gives the full path when the path is given in shortfroms such as tilde(~) or .. etc
                directory=os.path.expanduser(directory)
                try:
                    #chdir is a os library function used to change directories, always better to use functions than hardcoding the binary paths
                    os.chdir(directory)
                except OSError:
                    print(f"cd: {directory}: No such file or directory")


            case [comm,*args]:
                for path in paths:
                    #saving the execution path of the binary to a variable
                    execpath=f"{path}/{comm}"
                    if os.path.exists(execpath):
                        #using subproccess instead of os.system to properly give the arguments for the commands given
                        result=subprocess.run([comm] + args , executable= execpath)
                        #flag used here to denote that the command is valid and is executed and no need for command not found msg
                        flag=1
                        break
                if flag==0:
                    #when the command is not found in our list or the os binaries
                    print(f"{comm}: command not found")


if __name__ == "__main__":
    main()
