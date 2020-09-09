import pandas as pd
from collections import Counter
import sys

# reading data

data = pd.read_csv("data/data.csv")
print(type(data))


# checking if solved
def check_if_solved():
    if len(data.index) == 1:
        sys.exit(f"Your word is: {data.word.iloc[0]}")

    if len(data.index) == 0:
        sys.exit("Your Word does not exit is English Dictionary")

    if len(contains) + len(not_contains) >= 26:
        sys.exit("Your word does not exit.")


# End Goal Variables:

contains = []
not_contains = []

# step 1. filtering based on length. Dropping rows where length do not match user word length.

length = int(input("What is length of your Word? "))
data = data.drop(data[data["length"] != length].index)
check_if_solved()

# First guess_list is based on frequency of every words in English Language matched against in millions of books.
guess_list = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y',
              'b', 'v', 'k', 'x', 'j', 'q', 'z']

# To Run until solved.
while True:

    # Asking if certain letter exist in user's word.

    for letter in guess_list:
        if input(f"Does Your Word have {letter}: ") in ["True", "true", "yes", "Yes", "1", "y"]:
            contains.append(letter)
            guess = letter
            break
        else:
            not_contains.append(letter)

    # Dropping rows which does not contain guess letter.

    data = data.drop(data[data[f"{guess}"] == "-1"].index)
    check_if_solved()

    # Asking number of times guess letter exist.

    number_of_guess = int(input(f"number of {guess}: "))

    location = []

    # Asking location of guess letter.

    for _ in range(number_of_guess):
        location.append(int(input(f"location of {guess}: ")))
    location = tuple(location)

    # Dropping rows which does not contain exact word location.

    data = data.drop(data[data[f"{guess}"] != str(location)].index)
    check_if_solved()

    # making a list of remaining words -> str -> counting occurrence -> guess_list

    remaining_word_list = data["word"].tolist()
    remaining_word = "".join(remaining_word_list)

    x = Counter(remaining_word)

    guess_list = sorted(x, key=x.get, reverse=True)

    # removing contains and not_contains from guess list.

    guess_list = list(set(guess_list) - set(contains) - set(not_contains))
