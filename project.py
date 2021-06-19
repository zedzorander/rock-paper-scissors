import random

# create list
lst = ('r', 'p', 's')
beatsLst = ('p', 's', 'r')      # list that shows what beats each choice in lst
playerWins = False

# welcome user
print("Welcome to Cole's Rock, Paper, Scissors game!")

while playerWins != True:
    # ask user what to play
    print("Make your choice and then press enter...")
    print("r: Rock")
    print("p: Paper")
    print("s: Scissors")

    # get player input
    playerChoice = input().lower()
    if playerChoice != 'r' and playerChoice != 'p' and playerChoice != 's':
        print("Terrible choice. Try again.")
        continue

    # randomly choose for npc
    computerChoice = random.choice(lst)

    # display choices
    print("You played", playerChoice)
    print("The computer played", computerChoice)

    # get index locations for choices
    playerIndex = lst.index(playerChoice)
    computerIndex = beatsLst.index(computerChoice)

    # f computer wins
    if playerIndex == computerIndex:
        print("The computer wins. Please try again.")
    # if tie
    elif playerChoice == computerChoice:
        print("We have a tie. Please try again.")
    # if player wins
    else:
        print("Congratulations!! You won.")
        playerWins = True

    