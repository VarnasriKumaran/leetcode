class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row=len(matrix)
        col=len(matrix[0])
        target=[]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    target.append([i,j])
        for i in range(row):
            for j in range(col):
                if [i,j] in target:
                    for t in range(col):
                        matrix[i][t]=0
                    for r in range(row):
                        matrix[r][j]=0
                    
