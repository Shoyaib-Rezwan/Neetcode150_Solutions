class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        freq=[0]*10
        #check rows
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if freq[int(board[i][j])]==1:
                    return False
                freq[int(board[i][j])]=1
            for k in range(0,10):
                freq[k]=0
        #check columns
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i]==".":
                    continue
                if freq[int(board[j][i])]==1:
                    return False
                freq[int(board[j][i])]=1
            for k in range(0,10):
                freq[k]=0
        #check 3*3 squares
        for i in range(0,9,3):
            for j in range(0,9,3):
                for row in range (i,i+3):
                    for col in range(j,j+3):
                        if board[row][col]==".":
                            continue
                        if freq[int(board[row][col])]==1:
                            return False
                        freq[int(board[row][col])]=1
                for k in range (0,10):
                    freq[k]=0
        return True
board=[[] for _ in range(0,9)]
for i in range(0,9):
    board[i]=input().split()
print(Solution().isValidSudoku(board))
