class Customer:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def intro(self):
        print("i am",self.name,"and i am",self.age,"old")
c1=Customer("lio",20)
c2=Customer("li",40) 
c3=Customer("jay",12) 
l=[c1,c2,c3] 
for i in l:
    i.intro()