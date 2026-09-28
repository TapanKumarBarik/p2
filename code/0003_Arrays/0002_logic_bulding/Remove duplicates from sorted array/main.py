class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        n = len(nums)-1
        index = 0
        while i<n:
            if nums[i]!=nums[i+1]:
                nums[index] = nums[i]
                index+=1
            i+=1

        nums[index] = nums[n]
        index+=1
        return index



s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
length = s.removeDuplicates(nums)