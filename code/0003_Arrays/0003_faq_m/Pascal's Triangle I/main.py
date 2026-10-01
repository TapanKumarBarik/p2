class Solution:
    def pascalTriangleI(self, r, c):
        res = []

        for i in range(r):
            temp = [1]

            for j in range(1, i):
                temp.append(res[i-1][j-1] + res[i-1][j])

            temp.append(1)
            res.append(temp)

        return res[r-1][c-1]


s = Solution()
r=5
c=3
print(s.pascalTriangleI(r,c))