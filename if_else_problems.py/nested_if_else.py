# #gratest of 2 numbers 
# a = int(input("enter value of first number :"))
# b = int(input("enter value of second number :"))
# if a > b:
#     if b >a:
#         print("2nd entred nuber is gratest one :",b)
#     else:
#         print("1st entered number id gratest one :",a)
# else:
#     print("2nd one is gratest number:",b)

#gratest of 3numbers 
a = int(input("enter value of  1st number:"))
b = int(input("enter value of 2nd number: "))
c = int(input("enter value of 3rd number:"))
if a >= b  :
    if  a >= c :
        print("1st number is gratest number :",a)
    else:
        print("3rd number is grater",c)
else:
    if b > a:
        print("2nd number is gratest ",b)
    else:
        print("3rd number is gratest ",c)