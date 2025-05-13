"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    n=int(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    if(planet == "Mars"):
        weight = (n * 37.8)/100
    elif(planet == "Jupiter"):
        weight = (n * 236)/100
    elif(planet == "Venus"):
        weight = (n * 88.9)/100
    elif(planet == "Mercury"):
        weight = (n * 37.6)/100
    elif(planet == "Saturn"):
        weight = (n * 108.1)/100
    elif(planet == "Uranus"):
        weight = (n * 81.5)/100
    elif(planet == "Neptune"):
        weight = (n * 114)/100
    print("The equivalent weight on ",planet,": ",weight)

if __name__ == "__main__":
    main()