n1=int(input("enter fisrt number:"))
n2=int(input("ënter second number:"))
while true:
     choice=int(input("1.addition\n2.subtraction\n3.multiplication\n4.division\5.exit\nmake choice:\n"))
if(choice==1):
    print("sum=",n1+n2)
elif(choice==2):
    print("sub=",n1-n2)
elif(choice==3):
    print("mul=",n1*n2)
elif(choice==4):
    if(n2!=0):
        print("div=",n1/n2)
    else:
        print("division by zero error")
elif(choice==5):
    break       
else:
    print("ïnvalid choice")
