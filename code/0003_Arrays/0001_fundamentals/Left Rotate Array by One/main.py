class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        if n<=1:
            return nums
        start = nums[0]
        for i in range(n-1):
            nums[i]= nums[i+1]
        nums[n-1] = start
        return nums


s = Solution()
print(s.rotateArrayByOne([1,2,3,4,5]))
