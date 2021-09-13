"""Finding duplicate letters in a word."""

__author__ = "730529273"
word: str = input("Enter a word: ")
i: int = 0
dup: bool = False
while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            dup = True
        j = j + 1
    i = i + 1 
print("Found duplicate: " + str(dup))
