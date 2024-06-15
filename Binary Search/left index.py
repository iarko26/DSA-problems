def leftidx(arr,n,x):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            if mid==0 or arr[mid-1]!=x:
                return mid
            else:
                high=mid-1

            
        if arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[2, 2, 3, 3, 4,4,5]
n=len(arr)
x=4
print("Left index of element is",leftidx(arr,n,x))
