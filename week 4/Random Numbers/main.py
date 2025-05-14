import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    i=0
    while(i<10):
        value = random.randint(1, 100)
        print(value)
        i=i+1
    pass

if __name__ == '__main__':
    main()