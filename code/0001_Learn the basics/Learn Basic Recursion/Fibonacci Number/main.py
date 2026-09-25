class Solution:
    def fib(self, n):
        #your code goes here
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2) 
    
    
s = Solution()
n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in n_list:
    print(f"Fibonacci of {n} is: {s.fib(n)}")