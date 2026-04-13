n1 = int(input("enter your first number :"))
n2  = int(input("enter your second number :"))
choice = int(input("pls enter your choice from 1-5:"))
while True:
    if choice ==1:
        print("sum=",n1+n2)
    elif choice ==2:
        print("substrection = ", n1 - n2 )
    elif choice == 3:
        print("multiplication", n1 *n2)
    else:
        print(n1/n2)
        break