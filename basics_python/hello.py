# # x =10
# # y =14
# # z =36
# # print(x,y,z,sep="->")
# # ch= input("enter a chrecter")
# # print(ord(ch))
# # a =int(input("ascii value enter her :"))
# # print(chr(a))
# # f =["a","b","c","d"]
# # print("if d is prsent in f ","d"  in f)
# # print("if c is not prsent in f","c" not in f)
# # n =int(input("enter radiuese to calculate sphear area :"))
# # v =4/3*3.14*n*n
# # print("valume of sphear :",v)

# # m ="wellcome"
# # print(m)
# # print(type(m))
# # print(m[-9:-1])
# #m = "college is good"
# # n =m.endswith("good")
# # print(n)
# # n = m.capitalize()
# # print(n)
# # n =m.replace("good","luck")
# # print(n)
# # n =m.find("college")
# # print(n)
# # n = m.count("college")
# # print(n)

# l = ["bannana",20,"apple",30,"lemon",36]
# m =[10,35,36,25,84]
# # print(ll)
# # print(type(l))
# # n=l[2]
# # print(n)
# # k= l.append("vinayak")
# # print(k)
# # print(l)
# # print(m.sort())
# # print(m)
# # k= m.sort(reverse=True)
# # print(k)
# # print(m)
# # print(l.insert(2,"raju"))
# # print(l)
# # print(l[2:4])
# # print(l.remove("apple"))
# # print(l)
# # m.pop(2)
# # print(m)

# s= ("raju",35,4,2,15,1,5,"india")
# # print(s)
# # # print(type(s))
# # # k=s.index("india")
# # # print(k)
# # l= s.count(2)
# # print(l)
# # l = s.count(20)
# # print(l)
# # n = int(input("enter 1st :"))
# # m = int(input("enter 2nd :"))
# # k = int(input("enter 3rd"))
# # list = [n,m,k]
# # print(list)
# # w = list.sort(reverse=True)
# # print(w)
# # print(list)

# # iny = input("enter your input suprated by comma :")
# # numer = iny.split(",")
# # print(iny)

# #dictionary
# hi ={
#     "name":"raju",
#     "number":25,
#     "marks":[90,98,97]
# }
# # print(hi)
# # print(type(hi))
# # print(hi["marks"])
# # print(hi.get("name"))
# # l=hi.pop("marks")
# # print(l)

# #nested dictionary
# # dic = {
# #     "student" :"vinayak",
# #     "score": {
# #         "che":58,
# #         "phy":36,
# #         "bio":96
# #     }
# # }
# # print(dic)

# # ki ={
# #     "name":"shrvan",
# #     "marks": 20,
# #     "hight": 5
# # }
# # hi={
# #     "name":"raju"
# # }
# # print(ki)
# # print(ki["name"])
# # print(ki["marks"])
# # print(ki["hight"])
# # print(ki.keys())
# # print(ki.values())
# # print(ki.items())
# # print(ki.get("name"))
# # print(ki.get("value"))
# # print(ki.update(hi))
# # print(ki)
# #print(hi)
# #sets
# k ={1,"vinayak","rakesh","ramesh",20,36,30}
# l ={20,36,78,30}
# print(k)
# print(type(k))
# print(k.add("rani"))
# print(k)
# print(k.remove("vinayak"))
# print(k)
# l = k.clear()
# print(l)
# print(k)
# print(k.pop())
# print(k)
# l =[10,20,65,32]
# k =[35,85]
# # print(l.appen))
# # # print(l)
# # print(l.count(25))
# print(l.remove(10))
# print(l)
# j ={9,"9.0"}
# print(j)

# i=1
# while i<=10:
#     print(i**2)
#     i+=1

# for i in range(0,22,2):
#     print(i)
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)
# for i in range(10):
#     print("i passed")
# n = int(input("enter value of n "))
# sum=0
# for i in range(1,n+1):
#     sum = sum+i
#     print(i)
# print("SUM",sum)

# n = int(input("enter you nuber :"))
# sum =1
# for i in range(1,n+1):
#     sum*=i
# print(sum)

# n =int(input("enter value n:"))
# sum=1
# i=1
# while i<=n:
#     sum*=i
#     i+=1
# print(sum)

# def sum(n1,n2):
#     s =n1+n2
#     return s
# print(sum(1,2))

#recursion
# def hi(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*hi(n-1)