def main():
    stones = 20
    player = 1  # Start with Player 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        take = input(f"Player {player} would you like to remove 1 or 2 stones? ")

        while not take.isdigit() or int(take) not in [1, 2]:
            take = input("Please enter 1 or 2: ")

        take = int(take)
        stones -= take
        print()  # This ensures a blank line between turns

        if stones == 0:
            winner = 2 if player == 1 else 1
            print(f"Player {winner} wins!")
            break

        player = 2 if player == 1 else 1


if __name__ == '__main__':
    main()
