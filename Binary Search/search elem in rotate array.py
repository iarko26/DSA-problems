def elemrotate(arr,n,k):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=k and k<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=k and k<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

arr=[1]
n=len(arr)
k=0
print("Element found at index",elemrotate(arr,n,k))
