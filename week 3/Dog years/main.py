# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    age1= input("Enter an age in calendar years: ")
    age= int(age1)
    year = age*DOG_YEARS_MULTIPLIER
    print("That's ",year," in dog years!")
    pass  # Delete this line and write your code here! :)


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()