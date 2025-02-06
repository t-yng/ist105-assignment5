import random
import sys
import math


def to_numeric(value, name):
    try:
        return int(value)
    except ValueError:
        print(f"{name} is not numeric value.")
        exit(1)


number = to_numeric(sys.argv[1], "number")
text = sys.argv[2]

if text == "":
    print("Text is empty")
    exit(1)


def solve_number_puzzle(number: int):
    print("Number Puzzle: ")
    if number % 2 == 0:
        print(f"- The number {number} is even. Its square root is {math.sqrt(number)}.")
    else:
        print(f"- The number {number} is odd. Its square root is {number**3}.")


def solve_text_puzzle(text: str):
    print("Text Puzzle: ")
    binary = " ".join(format(ord(c), "b") for c in text)
    vowels = len(list(filter(lambda c: c in ["a", "i", "u", "e", "o"], text)))
    print(f"- Binary: {binary}")
    print(f"- Vowel Count: {vowels}")


def solve_treasure_hunt():
    print("Treasure Hunt: ")
    secret = random.randint(1, 100)
    guess = random.randint(1, 100)
    count = 1

    min_guess = 1
    max_guess = 100

    print(f"- The secret number is {secret}.")
    while secret != guess:
        if secret > guess:
            print(f"- Attempt {count}: {guess} (High!)")
            min_guess = guess + 1
        else:
            print(f"- Attempt {count}: {guess} (Low!)")
            max_guess = guess - 1

        guess = random.randint(min_guess, max_guess)
        count += 1
    else:
        print(f"- Attempt {count}: {guess} (Correct!)")
        print(f"- You found the treasure in {count} attempts!  ")


solve_number_puzzle(number)
print("")
solve_text_puzzle(text)
print("")
solve_treasure_hunt()
