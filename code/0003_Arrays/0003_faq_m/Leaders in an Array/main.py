class Solution:
    def leaders(self, nums):
        n = len(nums)
        if n==0:
            return nums
        res = []
        curr_max = nums[n-1]
        res.append(curr_max)
        for i in range(n-1, -1, -1):
            if nums[i]>curr_max:
                curr_max =  nums[i]
                res.append(curr_max)

        #return self.reverse(res)
        return res[::-1]

    def reverse(self, nums):
        start = 0
        end = len(nums)-1
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums 

s = Solution()
print(s.leaders([16, 17, 4, 3, 5, 2])) # Output: [17, 5, 2]
print(s.leaders([1, 2, 3, 4, 5])) # Output: [5]