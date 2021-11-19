i=1
sum=0
while i<=100:
    j=i
    while j<=i+10:
        if j>=0 and j<=10:
            sum=sum+j
            print(j)
        j=j+1
    break
i=i+1
print(sum)