import sys
import os

def main():
    # Wait for user input
    commands=['echo','exit','type']
    while(True):
        sys.stdout.write("$ ")
        flag=0
        command=input()
        if not command:
            continue
        match command.split():
            case ['exit','0']:
                sys.exit(0)
            case ['echo',*args]:
                print(*args)
            case ['type',arg]:
                if arg in commands:
                    print(f"{arg} is a shell builtin")
                else:
                    paths=os.getenv("PATH").split(":")
                    for path in paths:
                        if os.path.exists(f"{path}/{arg}"):
                            flag=1
                            print(f"{arg} is {path}/{arg}")
                            break
                
                    
                    if (flag==0):
                        print(f"{arg}: not found")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
