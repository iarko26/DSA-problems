class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            c_sum=nums[0]
            m_sum=nums[0]
            for num in nums[1:]:
                c_sum=max(num,c_sum+num)
                m_sum=max(c_sum,m_sum)
            return m_sum
        n_sum=kadane(nums)
        if max(nums)<0:
            return max(nums)
        
        t_sum=sum(nums)
        i_sum=[-num for num in nums]
        circular_sum=t_sum+kadane(i_sum)
        max_circular=max(n_sum,circular_sum)

      
        return max_circular

        
            



            

    
            
        
