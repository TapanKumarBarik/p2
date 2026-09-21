class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range (1,n):
            if nums[i-1]>nums[i]:
                j = i
                while j>0:
                    if nums[j-1]>nums[j]:
                        nums[j-1],nums[j] = nums[j],nums[j-1]
                    j-=1
        return nums



s = Solution()
nums = [64, 25, 12, 22, 11]
print(s.selectionSort(nums))