class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)
        
s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums))