# f = open("demo.txt","r")
# data =f.read()
# print(data)
# f.close()
# f = open("output.txt","r")
# data = f.read(10)
# print(data)
# print(type(data))
# f.close

with open("output.txt" ,"r") as f:
   data =f.read()
print(data)
print(type(data))