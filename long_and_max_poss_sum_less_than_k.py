def subarray(arr,k):
    n=len(arr)
    s=[]
    l=[]
    t=[]
    longest=0
    msub=float('-inf')
    for i in range(n):
        for j in range(i,n):
            a=arr[i:j+1]
            s.append(a)
    for i in s:
        p=sum(i)
        if p<k:
            if p>msub:
                msub=p
                l=[i]
            elif p==msub:
                l.append(i)
            if len(i)>longest:
                longest=len(i)
                t=[i]
            elif len(i)==longest:
                t.append(i)
    return s,msub,l,longest,t
m=list(map(int,input("Enter the array: ").split()))
k=int(input())
s,k,l,longest,t=subarray(m,k)
print("the subarrays are: ",s)
print("the max possible sum less than k is: ",k)
print("the sub array is",l)
print("longest subarray with sum less than k is: ",t)
print("length of the longest is: ",longest)
print(f"the count of the subarrays are: {len(s)}")
