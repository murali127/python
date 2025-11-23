def activity(arr):
    sarr=sorted(arr,key=lambda x:x[1])
    c=1
    le=sarr[0][1]
    for i in range(1,len(sarr)):
        if sarr[i][0]>=le:
            c+=1
            le=sarr[i][1]
    return c
    
n=int(input())
arr=[]
for _ in range(n):
    st,ed=map(int,input().split())
    arr.append((st,ed))
print(activity(arr))