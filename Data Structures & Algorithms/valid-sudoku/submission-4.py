class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        for row in range(n):
            seen=set()
            for j in range(n):
                if board[row][j]=='.':
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])

        for col in range(n):
            seen=set()
            for j in range(n):
                if board[j][col]=='.':
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        
        for sqre in range(n):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row= (sqre//3)*3+i
                    col=(sqre%3)*3+j
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

                                   


        