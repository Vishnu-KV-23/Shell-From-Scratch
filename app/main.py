import sys


def main():
    # Wait for user input
    flag=1
    while(flag):
        sys.stdout.write("$ ")
        command=input()
        match command.split():
            case ['exit','0']:
                sys.exit(0)
            case ['echo',*args]:
                print(*args)
            
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
