# n = int(input("enter value of n :"))
# i =1
# j=1
# while i<n+1:
#     i+=1
#     while j<n+1:
#         j+=1
#         print("*"*n,end=" ")
#         print()

#alpahbets by rows
n = int(input(" enter value of n :"))
i = 65
j = 65
while i<90+1:
    i+=1
    while j<90+1:
        j +=1
        print(chr(i)*n,end=" ")