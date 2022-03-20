import re

# Making an array with all of the English words
with open("words.txt", "r") as w:
    words = w.readlines()

# Creating variables
# Eighteen letters are allowed as the rest cannot be displayed on 7 segment displays. Letters "gkmqvwx" are ruled out
badLetters = "gkmqvwx"
longestAcceptableWord = ""

for tempWord in words:
    if len(tempWord) <= len(longestAcceptableWord):
        continue
    if re.search(tempWord, badLetters):
        break
    else:
        longestAcceptableWord = tempWord

print(longestAcceptableWord)
