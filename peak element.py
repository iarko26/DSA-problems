def peak(arr,n):
    if n==0:
        return -1
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
            return mid
        if arr[mid-1]<arr[mid]:
            low=mid+1
        else:
            high=mid-1

    return -1
arr=[1,2,1,2,1]
n=len(arr)
print("Peak element is",peak(arr,n))
