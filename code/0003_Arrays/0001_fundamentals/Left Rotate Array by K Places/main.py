class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k = k%n
        self.rotate(0,k-1,nums)
        self.rotate(k,n-1,nums)
        self.rotate(0,n-1,nums)
        return nums
    def rotate(self,start,end,nums):
        while start<=end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1


s = Solution()
nums = [1,2,3,4,5,6,7]
print(s.rotateArray(nums, 3))