class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        return n *  self.factorial(n-1)
    
    
s = Solution()
n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in n_list:
    print(s.factorial(n))