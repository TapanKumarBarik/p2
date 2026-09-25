class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n == 0:
            return
        print(n)
        self.printNumbers(n-1)
        
        
s = Solution()
s.printNumbers(10)