class Solution:
    def moveZeroes(self, nums):
        index = 0
        for i in nums:
            if i!=0:
                nums[index]= i
                index+=1
        for i in range(index, len(nums)):
            nums[i] = 0

        return nums
    
    
s = Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))