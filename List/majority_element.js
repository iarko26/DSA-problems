/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count=0
    let el
    let n=nums.length
    for(let i=0;i<n;i++){
        if(count===0){
            count=1
            el=nums[i]
            

        }
        else if(el===nums[i]){
            count++
        }
        else{
            count--
        }
      
    }
    let count1=0
    for(let i=0;i<n;i++){
        if(nums[i]===el){
            count1++
        }
    }
    if(count1>Math.floor(n/2)){
          return el
    }
    return -1
    

    
};