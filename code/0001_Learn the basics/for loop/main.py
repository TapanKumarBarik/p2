class Solution:
    def forLoop(self, low : int, high : int) -> int:
        # Your code goes here
        sum = 0
        for i in range (low , high+1):
            sum +=i
        return sum
    

sol = Solution()
result = sol.forLoop(1, 10)
print(result)