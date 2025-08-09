def fibo(n,d):
    if n in d:
        return d[n]
    else:
        d[n]=fibo(n-1,d)+fibo(n-2,d)
        return d[n]
d={0:1,1:1}
a=int(input())
print(fibo(a,d))
