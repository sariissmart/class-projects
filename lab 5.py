# x = 0
# while x < 10:
# print(x)
# x+=1
word = input("right a word \n")
counter = 0
hello = ["a","o","u","i","e"]
for letter in word:
    if letter in hello:
        counter+=1
print(word,"word has",counter,"vowels")

