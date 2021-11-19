n = int(input("enter the number : "))
row = 0
while row<n:
    star = row +1 
    while star > 0:
        print("*",end=" ")
        star = star - 1
    row = row + 1
    print()


# n = int(input("enter the number : "))
# i = 0
# while i <= n:
#     print("*"*i)
#     i = i + 1
# print()