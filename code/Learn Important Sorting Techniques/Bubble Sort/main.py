class Solution:
    def bubbleSort(self, nums):

        n = len(nums)

        for i in range(n-1):
            j=0
            while j<n-1-i:
                if nums[j]>nums[j+1]:
                    #swap
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                j+=1
        return nums
            

s = Solution()
nums = [7 ,4 ,1 ,5 ,3]
print(s.bubbleSort(nums))