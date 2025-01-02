n = int(input("Enter the number: "))
for i in range(1, n+1):
    print("*" * i)
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)

n = int(input("Enter the number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
n = int(input("Enter the number: "))
for i in range(1,n+1,1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n,0,-1):
    print(" " * (n-i)+"*" * (2*i-1))
print()
print("reverse star")
for i in range(n,0,-1):
        print(" "*(n-i)+"*"*(2*i-1))
print("binary stars")
for i in range(1,n+1,1):
        for j in range(i):
            print((i+j)%2,end=" ")
        print( )
print("double triangle")
for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" "*(n-i),end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print( )
