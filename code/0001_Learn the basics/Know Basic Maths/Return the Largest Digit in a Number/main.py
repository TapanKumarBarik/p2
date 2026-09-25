class Solution:
    def largestDigit(self, n):
        max_digit = 0
        while n>0:
            max_digit = max(max_digit, n%10)
            n = n//10
        return max_digit
    
    
s = Solution()
n_list = [12345, 24680, 13579, 11111, 22222]
for n in n_list:
    print(f"Largest digit in {n} is: {s.largestDigit(n)}")