a=float(input())
if a<0:
    print("-ve")
if a in [0,1]:
    print(a)
else:
    low,high=1,a 
    r=0
    p=0.0000001
    while (high-low)>p:
        mid=(low+high)/2 
        if mid * mid < a:
            low = mid
        else:
            high = mid
    print(f"{mid:2f}")
        