sum = 0
n = int(input("enter the number : "))
i = 1
while i <=n:
    if n % i == 0:
        sum = sum + 1
    i = i + 1
if sum == 2:
    print("prime number") 
else:
    print("not prime")