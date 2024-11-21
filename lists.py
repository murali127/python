#accessing
print("accessing")
l4=[[[1,2],[2,3]],[[5,6],[7,8]]]
print(l4[1][1][0])
l=[1,2,3,4,5]
print(l[::-1])


#editing
print("editing")
l[0]=3
print(l[0:4])


#add
print("add")
l.append(100)
l.append([5,6])
n=len(l)
print(l[0:n])

l.extend(["hello",134,143,23,4,50])
l.extend("murali")
n=len(l)
print(l[0:n])

l.insert(1,'Murali')
n=len(l)
print(l[0:n])


#Delete
print("delete")
del(l[0])
del(l[-6:])
l.remove("hello")
n=len(l)
print(l[0:n])
print(l.pop())
print("hello how are you".title())


#problem
#1

a="mrali dwnsfvnqw edfg ff"
print(a.split())
l=[]
for i in a.split():
    print(i.capitalize())
    l.append(i.capitalize())
print(l)
print(" ".join(l))


#2

email=input("enter the email: ")
a=email.find("@")
print(email[0:a])

#3

l=[1,1,2,2,3,3,4,4,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)