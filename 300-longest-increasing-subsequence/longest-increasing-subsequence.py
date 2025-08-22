class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        dp=[1]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

        # dp=[0]*len(nums)
        # first=nums[0]

        # for i in range(1,len(nums)):
        #     if first<nums[i]:
        #         dp[i]=dp[i-1]+1
        #     else:
        #         dp[i]=dp[i-1]
        #     first=nums[i]
        # return dp[len(nums)-1]+1
            







        # count=0
        # first=nums[0]

        # for i in range(1,len(nums)):
        #     if first<nums[i]:
        #         count+=1
        #     first=nums[i]
        # return count+1
        