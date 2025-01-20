import sys


def main():
    # Wait for user input
    commands=['echo','exit','type']
    while(True):
        sys.stdout.write("$ ")
        command=input()
        match command.split():
            case ['exit','0']:
                sys.exit(0)
            case ['echo',*args]:
                print(*args)
            case ['type',arg]:
                if arg in commands:
                    print(f"{arg} is a shell builtin")
                else:
                    print(f"{arg}: not found")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
