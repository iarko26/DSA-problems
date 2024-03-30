class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            return self.kthElement(arr2,arr1,m,n,k)
        low=max(0,k-m)
        high=min(k,n)
        
        while low<=high:
            i1=(low+high)//2
            i2=k-i1
            mdl1=float('-inf') if i1==0  else arr1[i1-1]
            mdr1=float('inf') if i1==n   else arr1[i1]
            mdl2= float('-inf') if i2==0 else arr2[i2-1]
            mdr2= float('inf') if i2==m  else arr2[i2]
            
            if mdl1<=mdr2 and mdl2<=mdr1:
                if i1+i2==k:
                    return max(mdl1,mdl2)
                else:
                    return min(mdr1,mdr2)
            elif mdl1>=mdr2:
                high=i1-1
            else:
                low=i1+1
                
