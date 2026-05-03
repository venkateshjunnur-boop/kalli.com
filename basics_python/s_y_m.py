n=6
marks=[]
print("enter the element:")
for i in range(n):
    mark=int(input())
    marks.append(mark)
for i in range(n):
    for j in range(0,n-i-1):
        if marks[j]<marks[j+1]:
            temp=marks[j]
            marks[j]=marks[j+1]
            marks[j+1]=temp
print("marks from high to low")
for i in range(n):
    print(marks[i])        

