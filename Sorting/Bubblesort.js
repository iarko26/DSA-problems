class Solution
{
   //Function to sort the array using bubble sort algorithm.
   bubbleSort(arr,n){
       for(let i=0;i<n-1;i++){
           let flag=false;
           for(let j=0;j<n-i-1;j++){
               if(arr[j+1]<arr[j]){
                   flag=true;
                   [arr[j+1],arr[j]]=[arr[j],arr[j+1]]
               }
           }
           if(!flag){
               break;
           }
       }
    //code here
   }
    
}