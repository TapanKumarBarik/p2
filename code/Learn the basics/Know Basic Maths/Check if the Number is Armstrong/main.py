class Solution:
    def isArmstrong(self, n):
        if n == 0:
            return True
        if self.calculte(n,len(str(n))) == n:
            return True
        return False
    
    def calculte(self,n,len_n):
        res = 0
        while n>0:
            temp_num = n%10
            n = n//10
            res+= temp_num**len_n
        return res
    
    
    
    
s = Solution()
n_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in n_list:
    if s.isArmstrong(n):
        print(f"{n} is Armstrong Number")
    else:
        print(f"{n} is not Armstrong Number")