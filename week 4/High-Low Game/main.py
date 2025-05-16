import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score = 0
    for i in range(0,5):
        print(f"Round {i+1}")
        n = random.randint(1,100)
        print(f"Your number is {n}")
        s = input("Do you think your number is higher or lower than the computer's?: ")
        a = random.randint(1,100)
        if(a>n):
            if(s == 'lower'):
                print(f"You were right! The computer's number was {a}")
                score = score + 1
                print(f"Your score is now {score}")
            else:
                print(f"Aww, that's incorrect. The computer's number was {a}")
                print(f"Your score is now {score}")
        else:
            if(s == 'higher'):
                print(f"You were right! The computer's number was {a}")
                score = score + 1
                print(f"Your score is now {score}")
            else:
                print(f"Aww, that's incorrect. The computer's number was {a}")
                print(f"Your score is now {score}")
        print("")
    print("Thanks for playing!")
    # TODO: Write your code here!!! :)

if __name__ == "__main__":
    main()