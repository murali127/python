##pass by refernece
class Customer:
    def __init__(self,name):
        self.name=name
def greet(customer):
    print(id(customer)) 
    customer.name="lii"   
    print(customer.name)
    print(id(customer))
cust=Customer("lio") 
print(id(cust))
greet(cust)
print(cust.name)