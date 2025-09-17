def bf(ml,c,f,i=0):
    if i==len(f) or ml==0:
        return 0
    nt=bf(ml,c,f,i+1)
    t=0
    if c[i]<=ml:
        t=f[i]+bf(ml-c[i],c,f,i+1)
    return max(nt,t)
def op(ml,c,f):
    n=len(f)
    d=[0]*(ml+1)
    for i in range(n):
        co=c[i]
        fu=f[i]
        for m in range(ml,co-1,-1):
            d[m]=max(d[m],fu+d[m-co])
    return d[ml]
ml=int(input())
c=list(map(int,input().split()))
f=list(map(int,input().split()))
print(bf(ml,c,f))
print(op(ml,c,f))
