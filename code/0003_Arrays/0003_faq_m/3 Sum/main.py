class Solution:
    def threeSum(self, nums: list) -> list[list]:

        n = len(nums)
        res = set()
        for i in range(n):
            
            for j in range(i+1,n):
                temp =[]
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] ==0:
                        temp = [nums[i], nums[j],nums[k]]
                        res.add(tuple(sorted(temp)))
        return [list(t) for t in res ]

        
s = Solution()
nums = [2, -2, 0, 3, -3, 5]
result = s.threeSum(nums)
print(result)