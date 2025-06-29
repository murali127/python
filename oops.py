class atm:
    __counter=1   #ststic variable

    def __init__(self):
        ##data
        #instance variables
        self.__pin = ""
        self.__balance = 0 
        self.sno=atm.__counter 
        atm.__counter=atm.__counter+1
        print(id(self))
        self.__menu()
    @staticmethod
    def get_counter():
        return atm.__counter
    @staticmethod 
    def set_counter(new):
        if type(new)==int:
            atm.__counter=new 
        else:
            print("not allowed")

    #getter
    def get_pin(self):
        return self.__pin
    #setter
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin 
            print("pin changed")
        else:
            print("Not allowed")
       ##methods 
    def __menu(self):
        while(True):
            user_input=input("""
            Hello how would like to proceed?
            1.Enter 1 to cerate pin
            2.Enter 2 to deposite 
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to get pin
            6.Enter 6 to set pin
            7.Enter 7 to exit
            """)
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=="5":
                print("the pin is => ",self.get_pin())
            elif user_input=="6":
                new_pin=input("enter the new pin => ")
                self.set_pin(new_pin)
            else:
                print("bye")
                break
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin set Successfully ")
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposit successfull")
        else:
            print("Incorrect pin")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance -= amount 
                print("Successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid Pin")        

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")
    
sbi = atm()
hdfc=atm()
print(sbi.sno)
print(hdfc.sno)
atm.set_counter("a")
print(atm.get_counter())