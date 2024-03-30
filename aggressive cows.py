def isvalid(stalls,n,k,mid):
    cows=1
    dis=0
    for i in range(n):
        if (stalls[i]-dis)>=mid:
            cows+=1
            if cows==k:
                return True
            dis=stalls[i]

    return False

def aggressivecows(stalls,k):
    stalls.sort()
    s=1
    n=len(stalls)
    e=stalls[n-1]-stalls[0]
    ans=0
    while s<=e:
        mid=(s+e)//2
        if (isvalid(stalls,n,k,mid)):
            ans=mid
            s=mid+1
        else:
            e=mid-1
    return ans
stalls=[6,4,0,3,4,7,10,9]
k=4
print(aggressivecows(stalls,k))





