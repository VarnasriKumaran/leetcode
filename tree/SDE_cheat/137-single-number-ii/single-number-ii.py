class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_nums=Counter(nums)
        for i in range(len(nums)):
            if count_nums[nums[i]]==1:
                return nums[i]
        return -1
