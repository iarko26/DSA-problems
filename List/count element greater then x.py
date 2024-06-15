
def greaterThanX(arr,x):
        
        
    count=0
    for i in arr:
        if i>x:
            count+=1
    return count
# Test the function
arr = [1, 3, 5, 2, 7, 4, 8]
x = 4

print(greaterThanX(arr,x))

