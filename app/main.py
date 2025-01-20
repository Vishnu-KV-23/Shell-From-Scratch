import sys


def main():
    # Wait for user input
    flag=1
    while(flag):
        sys.stdout.write("$ ")
        command=input()
        if not command:
            #sys.stdout.write("$ ")
            flag=0
        elif command=='exit 0':
            sys.exit(0)    
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
