#  P Pettran
# for row in range (7):
#     for col in range (5):
#         if col==0 or (col==4 and (row==1 or row==2)) or (row==0 or row==3) and (col>0 and col<4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# R print
# result_str="";    
# for row in range(0,9):    
#     for column in range(0,9):     
#         if (column == 1 or ((row == 0 or row == 4) and column > 1 and column < 6) or (column == 6 and row != 0 and row < 4) or (column == row - 1 and row > 3)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str)

# A Pettran
# for row in range(7):
#     for col in range (5):
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# T print
# for row in range (7):
#     for col in range (6):
#         if col==4 or (row==0 and col!=4):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()

# H Print
# for row in range (7):
#     for col in range(4):
#         if col==0 or col==3 or (row==3 and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# M print
# for row in range (7):
#     for col in range(7):
#         if col==0 or col==6 or (row==col) and (col>0 and col<4) or (row==1 and col==5) or (row==2 and col==4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# E Print
# for row in range (7):
#     for col in range(6):
#         if ((row==0 or row==3 or row==6)) or ((col==0 ) and (row!=0 and row!=3 and row!=6)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# S Print
# for row in range (7):
#     for col in range (5):
#         if ((row==0 or row==3 or row==6) and (col>0 and col<4))or col==0 and (row>0 and row<3) or (col==4 and (row>3 and row<6)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# I print
# for row in range (7):
#     for col in range (5):
#         if col==2 or (row==0 or row==6) and col!=2:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# N Print
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and (col>0 and col<5)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# n = int(input("enter the number : "))
# i = 0
# while i <= n:
#     print("*"*i)
#     i = i - 1
# print()


# num=int(input("enter the row number : "))
# row=0
# while row<num:
#     space=num-row-1
#     while space>0:
#         print(end=" ")
#         space=space-1
#     star=row+1
#     while star>0:
#         print(star,end=" ")
#         star=star-1
#     row=row+1
#     print()

# num=int(input("enter the number of rows : "))
# i=0
# while i<num:
#     i=i+1
#     print("$"*i)

# num=int(input("enter the number : "))
# i=0
# while i<num:
#     i=i+1
#     print(" "*(num-i)+"*"*i)