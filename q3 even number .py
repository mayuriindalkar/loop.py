i=20
sum=0
while i<=100:
    j=i
    while j<=i+20:
        if j%2==0:
            sum=sum+j
            print(j)
        j=j+1
    break
i=i+1
print(sum)