#general version of binary search
l=0
lst=list(map(int,input().split()))
r=len(lst)-1
n=int(input())
mid=0
while l<=r:
    mid=(l+r)//2
    if n>lst[mid]:
        l=mid+1
    elif n<lst[mid]:
        r=mid-1
    elif n==lst[mid]:
        print(f"value found at inadex {mid}")
        break
else:
    print("not found")



## recursive version of binary search
def bs(lst,l,r,n):
    if l > r:
        return -1
    mid=(l+r)//2
    if lst[mid]==n:
        return mid
    elif lst[mid]>n:
        return bs(lst,l,mid-1,n)
    elif lst[mid]<n:
        return bs(lst,mid+1,r,n)
lst=list(map(int,input().split()))
n=int(input())
idx=bs(lst,0,len(lst)-1,n)
if idx==-1:
    print("Not found")
else:
    print(f"found at {idx}")