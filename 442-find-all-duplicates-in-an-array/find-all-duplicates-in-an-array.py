class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return -1
        ans=set()
        out=[]

        for i in nums:
            if i in ans:
                out.append(i)
            else:
                ans.add(i)
        return out