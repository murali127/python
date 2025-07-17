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
print(len(L))
print(L.size)
print(L)