class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def backtrack(i,j,k):
            if k==len(word):
                return True
            if i<0 or i>=row or j<0 or j>=col or board[i][j]!=word[k]:
                return False

            temp=board[i][j]
            board[i][j]="#"

            found=(
                backtrack(i-1,j,k+1),
                backtrack(i+1,j,k+1),
                backtrack(i,j+1,k+1),
                backtrack(i,j-1,k+1),
            )
            board[i][j]=temp
            

            return any(found)

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False