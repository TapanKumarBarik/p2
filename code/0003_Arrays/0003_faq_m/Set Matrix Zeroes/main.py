class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        m = len(matrix)
        n  = len(matrix[0])

        first_row_zero = 1
        firs_col_zero =1 

        for i in range(m):
            if matrix[i][0]==0:
                firs_col_zero =0
                break
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero=0
                break
        
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0 :
                    matrix[i][j]=0

        if first_row_zero==0:
            for i in range(n):
                matrix[0][i]=0
        if firs_col_zero==0:
            for i in range(m):
                matrix[i][0]=0
        
        return matrix
        

                

s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
result = s.setZeroes(matrix)
print(result)