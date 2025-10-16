class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(op,start):
            if start== len(nums):
                ans.append(list(op))
                return 
            op.append(nums[start])
            backtrack(op,start+1)
            op.pop()
            backtrack(op,start+1)

        backtrack([],0)
        return ans