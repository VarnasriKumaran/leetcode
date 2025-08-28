class Solution:
    def issafe(self,board,row,col,n):
        for j in range(n):
            if board[row][j]=="Q":
                return False
        for j in range(n):
            if board[j][col]=="Q":
                return False

        i=row
        j=col
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1
        
        i=row
        j=col
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1
        return True



    def nQueen(self,board,row,n,ans):
        if row==n:
            ans.append(board[:])
            return 
            
        for j in range(n):
            if self.issafe(board,row,j,n):
                board[row]=board[row][:j]+'Q'+board[row][j+1:]
                self.nQueen(board,row+1,n,ans)
                board[row]=board[row][:j]+'.'+board[row][j+1:]





    def solveNQueens(self, n: int) -> List[List[str]]:
        board=["."*n for i in range(n)]
        ans=[]
        self.nQueen(board,0,n,ans)
        return ans
        