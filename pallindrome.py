word = str(input("Enter a word or number"))

word2 = "".join(reversed(word))
if str(word) == str(word2):
    print(f"{word} is pallindrome")
else:
    print(f"{word} is not pallindrome")
    




