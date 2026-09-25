class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n == 0:
            return
        
        self.printNumbers(n-1)
        print(n)
        
        
s = Solution()
s.printNumbers(10)