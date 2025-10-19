class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr=float(-inf)
        max_sum=float(-inf)
    
        for i in range(len(nums)):
            curr=max(curr+nums[i],nums[i])
            max_sum=max(curr,max_sum)
        return max_sum

        