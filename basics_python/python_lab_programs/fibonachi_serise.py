n =int(input("enter value of terns {n}:"))
a = 0
b = 1
if n<=0:
    print("invalide usered input please re-enter that  value grater than zero :")
else:
    print("the fibonach turns are the give by :")

    for i in range(n):
        print( a , end =" ")
    #calution parte 
        new = a+b
        a = b
        b  = new