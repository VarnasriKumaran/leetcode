class Solution:
    def func(self,start,ans,nums,sub):
        if start==len(nums):
            if sub not in ans:
                ans.append(list(sub))
            return 
        
        sub.append(nums[start])
        self.func(start+1,ans,nums,sub)

        sub.pop()
        self.func(start+1,ans,nums,sub)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        self.func(0,ans,nums,[])
        return ans
        