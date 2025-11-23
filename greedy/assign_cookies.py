
def findContentChildren(g, s):
    s.sort()
    g.sort()
    c=0
    l,r=0,0
    while l<len(g) and r<len(s):
        if g[l]<=s[r]:
            l+=1
        r+=1
    return l
g=list(map(int,input().split()))
s=list(map(int,input().split()))
print(findContentChildren(g,s))