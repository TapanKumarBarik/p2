class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1,n):
            for j in range(i, 0,-1):
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j] = nums[j], nums[j-1]
                else:
                    break
        return nums

            
s = Solution()
nums = [7 ,4 ,1 ,5 ,3]
print(s.insertionSort(nums))