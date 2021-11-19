# for row in range (7):
#     for col in range (5):
#         if col==0 or (col==4 and (row==1 or row==2)) or (row==0 or row==3) and (col>0 and col<4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str)

# N Print
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and (col>0 and col<5)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()