def ep(arr,n):
    total_sum=0
    left_sum=0
    n=len(arr)
    for i in range(n):
        total_sum+=arr[i] #this is the total sum of this array
    for i in range(n):
        total_sum-=arr[i] #this is for the right sum
        if left_sum==total_sum:
            return i
        left_sum+=arr[i]
    return -1
arr=[-7,1,5,2,-4,3,0]
n=len(arr)
result=ep(arr,n)
if result!=-1:
    print("The element is present at index",result)
else:
    print("Element is not present")

arr1 = [5, 1, 3, 5, 2, 2]
m=len(arr1)
res1=ep(arr1,m)
if res1!=-1:
    print("The element is present at index",res1)
else:
    print("Element is not present")

