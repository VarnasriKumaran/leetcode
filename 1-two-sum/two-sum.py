class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find=0
        ans=set()
        for i in range(len(nums)):
            find=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==find:
                    ans.add(i)
                    ans.add(j)
        ans=list(ans)
        return ans
