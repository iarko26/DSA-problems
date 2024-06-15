def Fmp(arr,n):
    n=len(arr)
    for i in range(n):
        elem=arr[i]
        while 1<=elem<=n and arr[elem-1]!=elem:
            arr[i],arr[elem-1]=arr[elem-1],arr[i]
            elem=arr[i]

            
            
                
            
                
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1
#test case
arr=[3,4,-1,1]
n=len(arr)
print(Fmp(arr,n))
#test  case 2
arr1=[1,2,0]
m=len(arr1)
print(Fmp(arr1,m))
                

