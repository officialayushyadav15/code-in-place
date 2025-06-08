"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: "))
    while (n != 1):
        m=n
        if(n%2==0):
            n=n//2
            print(f"{m} is even, so I take half: {n}")
        else:
            n=(3*n)+1
            print(f"{m} is odd, so I make 3n + 1: {n}")

    pass

if __name__ == "__main__":
    main()