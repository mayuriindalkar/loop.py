num=int(input("enter the number : "))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
i=1
while num>0:
    b=1
    while b<i:
        print(end=" ")
        b=b+1
    j=1
    while j<=num*1:
        print("*",end=" ")
        j=j+1
    print()
    num=num-1
    i=i+1