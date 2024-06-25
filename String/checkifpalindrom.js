function checkpal(arr){
   let l=-0;
  let  h=arr.length-1;
  while(l<h){
    if(arr[l]!==arr[h]){
        return false;
    }
    l++;
    h--;
  }
  return true;

 

    

}

console.log(checkpal("madam"));
console.log(checkpal("racecar"));
