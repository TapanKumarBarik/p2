class Solution:
    def countOddDigit(self, n):
        count = 0
        while n>0:
            if (n%10)&1 ==1:
                count+=1
            n = n//10
        return count
    
s = Solution()
n_list = [12345, 24680, 13579, 11111, 22222]
for n in n_list:
    print(f"Number of odd digits in {n} is: {s.countOddDigit(n)}")