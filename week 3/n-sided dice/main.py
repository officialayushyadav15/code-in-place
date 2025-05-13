import random

def main():
    side = int(input("How many sides does your dice have? "))
    n=random.randint(1,side)
    print("Your roll is ",n)

if __name__ == '__main__':
    main()