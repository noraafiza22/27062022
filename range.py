import random

def main():
    """Start a number guessing game between 1-100."""
    print("Guess the number!")

    x=(random.randrange(5,50))
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 5 to 50 :"))

        if x == guess:
            print("You genuis!")
        elif x > guess:
            print("Try a bigger number.")
        elif x < guess:
            print("Try a smaller number.")

main()