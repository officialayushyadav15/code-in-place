import random

def main():
    print("Khansole Academy")
    
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    
    print(f"What is {a} + {b}?")
    
    c = int(input("Your answer: "))
    if c == a + b:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {a + b}")
    
if __name__ == '__main__':
    main()
