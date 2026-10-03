class Solution:
    def rotateMatrix(self, matrix):

        #transpose
        # as it is n*n will make row as column and column as row
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] =matrix[j][i],matrix[i][j]
        
        # reverse

        for i in range(n):
            self.reverse(matrix[i])
        return matrix
    
    def reverse(self, matrix_row):
        i =0
        n = len(matrix_row)-1
        while i<n:
            matrix_row[i],matrix_row[n] = matrix_row[n], matrix_row[i]
            i+=1
            n-=1


s = Solution()
matrix = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]
print(s.rotateMatrix(matrix))