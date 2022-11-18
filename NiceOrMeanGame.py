#
# Python: 3.11.0
#
# Author: Vivian Pham
#
# Purpose: The Tech Academy - Python Course. Creating a program to demonstrate 
#          how to pass variables from function to function to create a game.
#





def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        check if this is a new game or not.
        If new - get user's name
        If not, thank the player for playing again
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean.")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name



def nice_mean (nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice or mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares aat you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # this passes the 3 variables to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the valie stored within the 3 variables
    if nice >2:
        win(nice,mean,name)
    if mean >2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("\nNice job {}, you win! \nYou are too friendly with everyone. \nBeware of strangers!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \nYou were too rude to strangers! \m{}, you will be wretched and alone! Get therapy".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO': \>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0 # not reseting name value since user will be playing again
    start(nice,mean,name)



    


if __name__ == "__main__":
    start()







