def slelem(arr):
    if len(arr) ==1:
        return -1
    elif not arr:
        return -1
    elif len(arr)<2:
        return -1
    else:
        lar=arr[0]
        slar=None or float('-inf')
        for i in arr[1:]:
            if i>lar:
                slar=lar
                lar=i
            elif i!=lar:
                if slar==None or slar<i:
                    slar=i
        if slar==float('-inf'):
            return -1
        return slar
arr=[12,10,20,34,50,50] #test case 1

print(slelem(arr)) 
arr_neg = [12,10,20,-34,50,50]
print(slelem(arr_neg))

    
                
                


        







