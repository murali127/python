#1. Create Node
class node:
    def __init__(self,value):
        self.data=value
        self.next=None
#2. Create Linked List
class ll:
    def __init__(self):
        self.head=None
        self.n=0 
#3. Length of linked list
    def __len__(self):
        return self.n
#4. Insertion from head
    def insert_head(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
#6. Insert from tail
    def insert_tail(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        self.n=self.n+1

#7. Insert at middle
    def insert_after(self,after,value):
        new_node=node(value)
        curr=self.head 
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next 
        if curr!=None:
            new_node.next=curr.next 
            curr.next=new_node
            self.n=self.n+1
        else:
            print('Item not found')
#5. Traverse
    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end="->")
            curr=curr.next 
        print("null") 
#6. Empty 
    def empty(self):
        self.head=None 
        self.n=0

L=ll()
while True:
    print(" ")
    print("Linked list operations to perform")
    print(" ")
    print("1. Length")
    print("2. Insert Head")
    print("3. Insert From Tail")
    print("4. Insert at Middle")
    print("5. Traverse the list")
    print("6. Empty")
    print("10. Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("the len of the ll is ", len(L))
    elif choice==2:
        a=int(input("enter the vlaue to insert : "))
        L.insert_head(a)
    elif choice==3:
        a=int(input("enter the vlaue to insert : "))
        L.insert_tail(a)
    elif choice==4:
        aft=int(input("enter thre after number :"))
        a=int(input("enter the vlaue to insert : "))
        L.insert_after(aft,a)
    elif choice==5:
        L.traverse()
    elif choice==6:
        L.empty()
    elif choice==10:
        print("ok byee")
        break