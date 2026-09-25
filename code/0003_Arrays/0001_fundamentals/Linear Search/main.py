class Solution:
    def linearSearch(self, nums, target):

        for i in range(len(nums)):
            if nums[i]==target:
                return i
        
        return -1



s = Solution()
nums = [1, 2, 3, 4, 5]
target = 3
result = s.linearSearch(nums, target)
print(result)