class Solution:
    def secondLargestElement(self, nums):
        max_num = max(nums)
        new_max_num = min(nums)
        if max_num == new_max_num:
            return -1
        for num in nums:
            if num!=max_num:
                new_max_num = max(new_max_num,num)
        return new_max_num


solution = Solution()
print(solution.secondLargestElement([3, 1, 4, 1, 5, 9, 2, 6]))