class Solution:
    def selectionSort(self, nums):
        index = 0
        n = len(nums)
        for i in range(n):
            curr_min=nums[i]
            swap_required = False
            for j in range(i,n,1):
                if nums[j]<curr_min:
                    curr_min=nums[j]
                    index = j
                    swap_required = True
            if swap_required:
                temp = nums[i]
                nums[i]=curr_min
                nums[index] = temp
        return nums



s = Solution()
nums = [64, 25, 12, 22, 11]
print(s.selectionSort(nums))