# Last updated: 9/12/2025, 8:36:46 PM
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
        