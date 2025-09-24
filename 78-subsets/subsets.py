class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)

        def backtrack(op,start):
            if start ==n :
                ans.append(list(op))
                return 
            
            op.append(nums[start])
            backtrack(op,start+1)
            op.pop()
            backtrack(op,start+1)


        backtrack([],0)
        return ans
        # ans.append([])
        # ans.append(nums)
        # for i in range(len(nums)):
        #     ans.append([nums[i]])

        # for i in range(len(nums)):
        #     temp=[]
        #     for j in range(i+1,len(nums)):
        #         temp=[nums[i],nums[j]]
        #         if temp not in ans:
        #             ans.append(temp)
        # return ans


        