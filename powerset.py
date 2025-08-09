def ps(n,d):
    k=tuple(n)
    if k in d:
        return d[k]
    if not n:
        return [[]]
    else:
        wl=ps(n[:-1],d)
        l=[s+[n[-1]]for s in wl]
        d[k]=wl+l 
    return d[k]
d={}
a=list(map(int,input().split()))
print(ps(a,d))
