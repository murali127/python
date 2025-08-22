import cmath
def taylor(x,terms=30):
    r=1.0
    t=1.0
    for n in range(1,terms):
        t*=x/n
        r+=t
    return r
def newton(x,iterations=25):
    if x<0:
        print("negative value")
    y=x-1.0
    for _ in range(iterations):
        y-=(taylor(y)-x)/taylor(y)
    return y
def int_pow(base,exp):
    r=1
    x=abs(base)
    e=exp
    while e>0:
        if e%2==1:
            r*=x
        x*=x
        e//=2
    return r
def getpow(a,b):
    if a==0:
        return 0 if b>0 else "undefined"
    if float(b).is_integer():
        ib = int(b)
        result = int_pow(abs(a), ib)
        return -result if (a < 0 and ib % 2) else result
    if a>0:
        return taylor(b*newton(a))
    else:
        print(f"this code is not taking the input as ({a}), so we are not getting a complex number output,____this {cmath.exp(b * cmath.log(a))} is the exact value calculated with cmath function")

        return -(taylor(b*newton(abs(a))))
a=float(input("enter the base: "))
b=float(input("enter the power: "))
print(getpow(a,b))
