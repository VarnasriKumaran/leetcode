class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        res=[]

        n=len(grid)
        m=len(grid[0])
        for i in grid:
            for j in i:
                if j not in ans:
                    ans.append(j)
                else:
                    res.append(j)

        max_num=n*m
        for i in range(1,max_num+1):
            if i not in ans:
                res.append(i)
        return res
        