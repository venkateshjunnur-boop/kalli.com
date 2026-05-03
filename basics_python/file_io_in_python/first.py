with open("/workspaces/kalli.com/basics_python/file_io_in_python/linux.txt","w") as f:
    data = f. write("Hi everyone\nwe are learning file I/O\nusing java\ni like programming in Java")
    print(data)
with open("/workspaces/kalli.com/basics_python/file_io_in_python/linux.txt","r") as f :
    path = f.read()
    print(path)
    new = path.replace("java","python")
    print(new)