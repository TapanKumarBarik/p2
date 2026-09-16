import math
class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        #your code goes here
        for i in range(2 , int(math.sqrt(n))+1,1):
            if n%i == 0:
                return False
        return True
    
    
s = Solution()
n_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in n_list:
    if s.isPrime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")