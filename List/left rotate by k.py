#brute force solution
# def leftrotatek(arr,k,n):
    
#     k=k%n
#     temp=[0]*k
#     for i in range(0,k):
#         temp[i]=arr[i]
#     for i in range(k,n):
#         arr[i-k]=arr[i]
#     for i in range(n-k,n):
#         arr[i]=temp[i-(n-k)]
#     return arr
# arr=[1,2,3,4,5,6,7]
# k=3
# n=len(arr)
# print(leftrotatek(arr,k,n))

#optimal solution
def leftrotatek(arr,k,n):
    k=k%n
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    arr[:]=reversed(arr)
    return arr

arr=[1,2,3,4,5,6,7]
k=3
n=len(arr)
print(leftrotatek(arr,k,n))

        
            



    

    

    