n = int(input("enter value of n :"))
for i in range(n,0,-1):
    for j in range(1,2*i-n):
        print("*",end = " ")
    print()