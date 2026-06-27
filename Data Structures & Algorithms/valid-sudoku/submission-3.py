class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        col=[0]*n
        row=[0]*n
        for i in range(n):
            col=[0]*n
            for k in range(n):
                element=board[k][i]
                if element=='.':
                    element=0
                else: element=int(board[k][i])
                if (element in col) and (element!=0) :
                    col[k]=element
                    print('repeat in column number'+ str(k)+'repeated number is '+ str(element))
                    print(col)
                    return False
                else:
                    col[k]=element
                    
                    
            row=[0]*n
            for j in range(n):
                element=board[i][j]
                if element=='.':
                    element=0
                else: element=int(board[i][j])
                if (element in row) and element!=0:
                    print('repeat in row'+str(j)+'repeated number is '+ str(board[i][j]))
                    print(row)
                    return False
                else: 
                    row[j]=element
            sqre=[0]*n
            idx=0
            for srow in range(3):
                for scol in range(3):
                    brow=(i//3)*3+srow
                    bcol=(i%3)*3+scol
                    element=board[brow][bcol]
                    if element=='.':
                        element=0
                    else: element=int(board[brow][bcol])
                    
                    if element in sqre and element !=0:
                        return False
                    else:
                        sqre[idx]=element
                        idx+=1



        

        print(row)
        print (col)
        print('checked row and column')
        return True

        