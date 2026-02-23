n = int(input("enter value of n "))
k = range(1,n+1)
sum = 0
for i in k:
    sum = sum+i
    if(i==n):
        print(sum)