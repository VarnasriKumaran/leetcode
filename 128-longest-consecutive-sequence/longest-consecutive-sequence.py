class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        temp=0
        nums=set(nums)
        nums=sorted(nums)
        if not nums:
            return 0
        first=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==first+1:
                count+=1
            else:
                temp=max(count,temp)
                count=1
            first=nums[i]
        count=max(count,temp)
        return count

        