/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let j=-1
    for(let i=0;i<nums.length;i++){
        if(nums[i]===0){
            j=i
            break;
        }
    }
    if(j==-1) return;
    for(let i=j+1;i<nums.length;i++){
        if(nums[i]!==0){
            [nums[j],nums[i]]=[nums[i],nums[j]]
            j++
           
        }

    }

   

    
    
};