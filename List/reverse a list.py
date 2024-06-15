def revlist(l):
    start=0 
    end=len(l)-1

    
    while start<end:
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
    return l

    


l=[10,20,40,30,50]
result=revlist(l)

print(result)