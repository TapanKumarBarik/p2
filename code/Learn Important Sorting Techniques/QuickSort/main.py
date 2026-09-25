class Solution:
    def quickSort(self, nums):
        n = len(nums)
        if n<=1:
            return nums
        
        self.sort(nums, 0,n-1)
        
        return nums
    
    def sort(self, nums, start, end):
        if start>=end:
            return
        
        pivot_index = self.partition(nums, start, end)

        self.sort(nums, start, pivot_index-1)
        self.sort(nums, pivot_index+1, end)
    
    def partition(self, nums, start, end):

        pivot = nums[end]

        i = start
        for j in range(start, end):
            if nums[j]<pivot:
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
        nums[i], nums[end] = nums[end], nums[i]
        return i






solution = Solution()
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = solution.quickSort(nums)
