n = int(input("enter value of n :"))
a = 0
b = 1
if n <=0:
    print("opration dose not proceess")
else:
    print("the lenght of fibonachi sequence is =")
    for i in range(n):
     print(a,end =",")
     c = a + b 
     a = b 
     b = c 
