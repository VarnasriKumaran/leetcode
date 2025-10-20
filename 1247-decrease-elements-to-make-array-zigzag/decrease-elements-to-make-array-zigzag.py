# cook your dish here
class Solution:
    def movesToMakeZigzag(self, nums):
        n=len(nums)
        even=0
        for i in range(0,n,2):
            d=0
            if i-1 >=0 and nums[i]>=nums[i-1]:
                d=max(d,nums[i]-nums[i-1]+1)
            if i+1<n and nums[i]>=nums[i+1]:
                d=max(d,nums[i]-nums[i+1]+1)
            even+=d

        odd=0
        for i in range(1,n,2):
            d=0
            if i-1 >=0 and nums[i]>=nums[i-1]:
                d=max(d,nums[i]-nums[i-1]+1)
            if i+1<n and nums[i]>=nums[i+1]:
                d=max(d,nums[i]-nums[i+1]+1)
            odd+=d
        return min(odd,even)













        #     if i%2!=0:
        #         if nums[i-1] <= nums[i]:
                    
        #             while(nums[i]>=nums[i-1]):
        #                 nums[i]-=1
        #                 count+=1
        #     if i%2==0:
        #         if nums[i-1] >= nums[i]:
        #             while(nums[i]<=nums[i-1]):
        #                 nums[i]+=1
        #                 count+=1

        # return count

        