# f = open("/workspaces/kalli.com/basics_python/file_io_in_python/demo.txt","r")

# line1 = f.readline()
# print(line1)

# print(type(line1))
# print(line1)


# f.close

f = open("demo.txt","r")
data =f.read()
print(data)
f.close()

