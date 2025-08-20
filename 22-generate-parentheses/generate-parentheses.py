class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(res,open,close):
            if len(res)==2*n:
                ans.append(res)
                return 
            if open<n:
                backtrack(res+"(",open+1,close)
            if open> close:
                backtrack(res+")",open,close+1)
        ans=[]
        backtrack("",0,0)
        return ans

