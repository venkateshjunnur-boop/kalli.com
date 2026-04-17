import math
N = int(input("enter the terms in list :"))
numbers =[]
for i in range(N):
    num =float(input("enter a numbers :"))
    numbers.append(num)
mean =sum(numbers)/N
var = sum((x-mean)**2 for x in numbers)/N
sd = math.sqrt(var)
print(numbers)
print("mean =",mean)
print("variance=",var)
print("sd=",sd)