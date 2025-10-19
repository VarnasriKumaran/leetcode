class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return None
        curr=sum(nums[:k])
        max_avg=curr/k
        for i in range(k,len(nums)):
            curr=curr+nums[i]-nums[i-k]
            max_avg=max(max_avg,curr/k)
        return max_avg