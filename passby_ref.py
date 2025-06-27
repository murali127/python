##pass by refernece
class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer.gender=="Male":
        print("helo",customer.name," sir")
    else:
        print("helo",customer.name," mam")
    cust3=Customer("li","Male")
    return cust3
cust1=Customer("lio","Male") 
cust2=Customer("oil","Female")
new_cust=greet(cust1)
greet(cust2)
print(new_cust.name)