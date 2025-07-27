##Sample example of creating a linked list how it works

class node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
print(a.next)