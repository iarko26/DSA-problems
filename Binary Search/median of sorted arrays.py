def mediansort(a1,a2):
    n1,n2=len(a1),len(a2)
    if n1>n2:
        return mediansort(a2,a1)
    low=0
    high=n1
    while low<=high:
        i1=(low+high)//2
        i2=(n1+n2+1)//2-i1
        mdl1=float('-inf') if i1==0 else a1[i1-1]
        mdr1=float('inf') if i1==n1 else a1[i1]
        mdl2= float('-inf') if i2==0 else a2[i2-1]
        mdr2= float('inf') if i2==n2 else a2[i2]
        if mdl1<=mdr2 and mdl2<=mdr1:
            if (n1+n2)%2==0:
                return (max(mdl1,mdl2)+min(mdr1,mdr2))/2
            else:
                return max(mdl1,mdl2)
        elif mdl1>mdr2:
            high=i1-1
        else:
            low=i1+1
    return -1
a1=[1,2]
a2=[3,4]
print(mediansort(a1,a2))


 

        
