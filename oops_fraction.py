class fraction:
    def __init__(self,n,d):
        self.num=n 
        self.den=d 
    def display(self):
        print(f"{self.num}/{self.den}={self.num/self.den}")
    def __str__(self):
        return str(self.num / self.den) #print inbuilt And also can be written asreturn "{}/{}".format(self.num,self.deno)
    def __add__(self,o):
        temp_num=self.num*o.den+o.num*self.den 
        temp_den=self.den*o.den
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self,o):
        temp_num=self.num*o.den-o.num*self.den 
        temp_den=self.den*o.den
        return "{}/{}".format(temp_num,temp_den)
    def __mul__(self,o):
        temp_num=self.num*o.num
        temp_den=self.den*o.den
        return "{}/{}".format(temp_num,temp_den)
    def __truediv__(self,o):
        temp_num=self.num*o.den
        temp_den=self.den*o.num
        return "{}/{}".format(temp_num,temp_den)
nume=int(input("enter the numerator :"))
deno=int(input("enter the denominator :"))
f1=fraction(nume,deno)
f1.display()
nume2 = int(input("Enter the numerator for f2: "))
deno2 = int(input("Enter the denominator for f2: "))
f2 = fraction(nume2, deno2)
f2.display()
print(f"using string magic method {nume}/{deno} =",f1)
print(f"Addition of f1 + f2 = {f1 + f2}")
print(f"sub of f1 - f2 = {f1 - f2}")
print(f"mul of f1 X f2 = {f1 * f2}")
print(f"mul of f1 / f2 = {f1 / f2}")