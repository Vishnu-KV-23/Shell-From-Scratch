import sys
import os
import subprocess

def main():
    # Wait for user input
    commands=['echo','exit','type','pwd','cd']
    paths=os.getenv("PATH").split(":")
    while(True):
        sys.stdout.write("$ ")
        flag=0
        command=input()
        if not command.strip():
            continue
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
                            #print(f"{arg} is a shell builtin")
                            print(f"{arg} is {path}/{arg}")
                            break
                
                    
                    if (flag==0):
                        print(f"{arg}: not found")
            case ['pwd']:
                print(os.getcwd())
            case ['cd',directory]:
                try:
                    os.chdir(directory)
                except OSError:
                    print(f"cd: {directory}: No such file or directory")


            case [comm,*args]:
                for path in paths:
                    execpath=f"{path}/{comm}"
                    if os.path.exists(execpath):
                        result=subprocess.run([comm] + args , executable= execpath)
                        flag=1
                        break
                if flag==0:
                    print(f"{comm}: command not found")


if __name__ == "__main__":
    main()
