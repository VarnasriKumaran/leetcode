# Last updated: 9/12/2025, 9:46:57 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j=0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

