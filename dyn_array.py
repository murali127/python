import ctypes
class ml:
    def __init__(self):
        self.size=1
        self.n=0
#1. creating an array with size of self.size
        self.a=self.__make_array(self.size)
#2. length
    def __len__(self):
        return self.n
#3. append
    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)
        #append
        self.a[self.n]=item
        self.n=self.n+1
#4. Print
    def __str__(self):
        res=''
        for i in range(self.n):
            res=res+str(self.a[i])+ ','
        return '['+ res[:-1] +']'
#5. Indexing 
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.a[index]
        else:
            return 'Indexerror - Index out of range'
#6. Pop 
    def pop(self):
        if self.n==0:
            return 'Empty List'
        print(self.a[self.n-1])
        self.n=self.n-1
#7. Clear
    def clear(self):
        self.n=0
        self.size=1
#8. Find
    def find(self,item):
        for i in range (self.n):
            if self.a[i]==item:
                return i 
        return 'not in list'

#9. Insert 
    def insert(self,pos,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos-1):
            self.a[i]=self.a[i-1]
        self.a[pos]=item 
        self.n=self.n+1
#10. Delete 
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.a[i]=self.a[i+1]
            self.n=self.n-1
#11. Remove 
    def remove(self,item):
        pos=self.find(item)
        if type(pos)==int:
            self.__delitem__(pos)
        else:
            return pos
    def __resize(self,new_capacity):
        #create array with new capacity
        b=self.__make_array(new_capacity)
        self.size=new_capacity
        #copy contents to b 
        for i in range(self.n):
            b[i]=self.a[i]
        #ressiagn a 
        self.a=b

    def __make_array(self,capacity):
        #creates a ctype array with size capacity (it is alsoa ref array )
        return(capacity*ctypes.py_object)()
L=ml()
L.append("Lio")
L.append(3.4)
L.append(True)
L.append(100)
L.append(1)
L.append(45)
print(len(L))
print(L.size)
print(L)
print(L[10])
L.pop()
print(L)
L.insert(5,45)
print(L)
print(L.find(100))
del L[6]
print(L)
L.clear()
print(L)
L.insert(0,0)
L.remove(0)
print(L)
