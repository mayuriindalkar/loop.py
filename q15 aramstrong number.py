a=int(input("Enter the number : "))
sum=0
i=a
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if sum==a:
    print("Number is armstrong")
else:
    print("Number is not armstrong")


# a = int(input("enter the number : "))
# i = a
# count = 0
# while i > 0:
#     count = count + 1
#     i = i // 10
# sum = 0
# i = a
# while i > 0:
#     digit = i % 10
#     x = 1
#     pro = 1
#     while x<=count:
#         pro = pro * digit
#         x = x + 1
#     sum = sum + pro
#     i = i // 10
# if sum == a:
#     print("armstrong number")
# else:
#     print("not armstrong number")
