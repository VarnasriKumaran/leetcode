class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=set()
        if not nums:
            return -1

        for i in nums:
            if i in ans:
                return i
            else:
                ans.add(i)
        return -1
        