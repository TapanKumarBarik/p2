class Solution:
    def GCD(self, n1, n2):
        num = min(n1,n2)
        while num>1:
            if (n1%num == 0) and (n2%num) == 0:
                return num 
            num-=1
        return num
    
    
s = Solution()
print(s.GCD(12, 18))
    