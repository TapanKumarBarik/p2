class Solution:
    def largestElement(self, nums):
        max_num =nums[0]
        for num in nums:
            max_num = max(max_num, num)
        return max_num
        
        
        
s = Solution()
nums = [1, 2, 3, 4, 5]
result = s.largestElement(nums)
print(result)
