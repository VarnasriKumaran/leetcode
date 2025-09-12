# Last updated: 9/12/2025, 8:45:29 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=0
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return -1
        