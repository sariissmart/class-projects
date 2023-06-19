# user = int(input("choose first number"))
# inp = int(input("choose second number"))
# for x in range(user,inp):
#     if x % 2 == 0:
#         print(x)
#     if x == 2 or x == 4:
#         break
x=-100000000
user = int(input("choose first number"))
inp = int(input("choose second number"))
while x >= user and x <=inp:
    if x % 2 == 0:
        print(x)
    if x == 2 or x == 4:
        break
    x+=1


