/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let N=nums.length
    let summ=(N*(N+1))/2
    let s2=0
    for(let i=0;i<N;i++){
        s2+=nums[i]
    }
    let missingNum=summ-s2
    return missingNum
    
};