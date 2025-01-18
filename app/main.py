import sys


def main():
    # Wait for user input
    flag=1
    while(flag):
        sys.stdout.write("$ ")
        command=input()
        while not command:
            #sys.stdout.write("$ ")
            flag=0
            
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
