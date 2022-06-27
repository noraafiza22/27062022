import random

def main():
    """Start a periodic table guessing game."""
    print("Guess the element!")

    element = [
        "sodium",
        "zinc",
        "copper",
        "bromine",
        "barium",
        "radium",
        "nickel"
        ]

    x = random.choice(element)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()