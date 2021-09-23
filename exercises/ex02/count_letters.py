"""Counting letters in a string."""
__author__ = "730529273"
letter_input: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
counter: int = 0
while i < len(word):
    if letter_input == word[i]:
        counter = counter + 1
    i = i + 1
print("Count: " + str(counter))