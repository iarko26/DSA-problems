class Solution
{
    partition(arr, low, high){
       let pivot=arr[low];
        let i=low;
        let j=high;
        while(i<j){
            while(arr[i]<=pivot){
                i++;
            }
            while(arr[j]>pivot){
                j--;
            }
            if(i<j){
                [arr[i], arr[j]] = [arr[j], arr[i]]; 
            }
        }
        [arr[low], arr[j]] = [arr[j], arr[low]];
        return j;
        
        
        
    }
    
    quickSort(arr, low, high){
        if(low<high){
            let pivot=this.partition(arr,low,high)
                this.quickSort(arr,low,pivot-1)
                this.quickSort(arr,pivot+1,high)
        
            }
        }
        
    }
    
