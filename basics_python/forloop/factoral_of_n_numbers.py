n = int(input("enter value of n :"))
k = range(1,n+1)
fact =1
for i in k:
    fact = fact*i
    print("sum thse all >>>>",i)
    if(i==n):
        print(fact)