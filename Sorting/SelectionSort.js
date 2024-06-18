class Solution
{
  select(arr,i){
       let min_index=i
      for(let j=i+1;j<arr.length;j++){
          if(arr[j]<arr[min_index]){
              min_index=j
          }
      }
      return min_index
      
      
     
  }

  //Function to sort the array using selection sort algorithm.
  selectionSort(arr,n){
      for(let i=0;i<n-1;i++){
          let min_index=this.select(arr,i)
          if (min_index !== i) {
        [arr[min_index], arr[i]] = [arr[i], arr[min_index]];
      }       
          
      }
      
   
  }
    
}