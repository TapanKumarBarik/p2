class Solution:
    def pascalTriangleIII(self, n):
        res =[]
        for i in range(n):
            temp =[1]
            
            for j in range(1,i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            
            if i!=0:
                temp.append(1)
            res.append(temp)
        return res 
    
s = Solution()
n=5
print(s.pascalTriangleIII(n))