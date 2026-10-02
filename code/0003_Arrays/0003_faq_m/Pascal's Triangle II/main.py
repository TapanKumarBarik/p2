class Solution:
    def pascalTriangleII(self, r):

        res =[]
        for i in range(r):
            temp =[1]
            
            for j in range(1,i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            
            if i!=0:
                temp.append(1)
            res.append(temp)
        return res[r-1] 
        
        
s = Solution()
r=6
print(s.pascalTriangleII(r))