#word = str(input("Enter a word or number"))


# word2 = "".join(reversed(word))
# if str(word) == str(word2):
#     print(f"{word} is pallindrome")
# else:
#     print(f"{word} is not pallindrome")
    
#try by creating function my self in main 2
word = str(input("Enter a word or number :"))
b=[]
def reverse(a):
    for i in range(len(a)):     #for reverse used word2= word[::-1]
        b.append(a[i])
    return "".join(b)
word2= reverse(word)
print(word2)
if str(word2) == str(word):
    print(f"{word} is pallindrome")
else:
    print(f"{word} is not  pallindrome")





