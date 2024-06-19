class Solution {
    //Function to sort the binary array.
    binSort(A, N)
    {
        let l=0;
        let r=N-1
        while(l<r){
            while(l<r && A[l]===0){
                l++;
            }
            while(l<r && A[r]===1){
                r--;
            }
            
            if(l<r){
             [A[l], A[r]] = [A[r], A[l]];
             l++;
             r--;

            }
        }
        
    }
}