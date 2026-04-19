num = input("enter the numbers :")
freq ={}
for digit in num:
    if digit in freq:
        freq(digit)+=1
    else:
        freq(digit)=1
for key , value in freq:
    print(key ":" value )