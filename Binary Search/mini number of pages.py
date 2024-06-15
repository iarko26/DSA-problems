def isvalid(arr,n,m,mid):
    req=1
    s=0
    for i in range(n):
        if(s+arr[i])>mid:
            req+=1
            s=arr[i]
        else:
            s+=arr[i]
    return req<=m





def findPages(arr: int, n: int, m: int) -> int:
    if m>n:
        return -1
    n=len(arr)
    s=sum(arr)
    mx=max(arr)
    low=mx
    high=s
    res=0
    while low<=high:
        mid=(low+high)//2
        if(isvalid(arr,n,m,mid)):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res
    


    