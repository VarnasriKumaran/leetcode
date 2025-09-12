# Last updated: 9/12/2025, 9:39:44 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans=[]
        count=0
        for i in nums:
            if i == 0:
                count+=1
            else:
                ans.append(i)


        for i in range(count):
            ans.append(0)
        
        for i in range(len(ans)):
            nums[i]=ans[i]