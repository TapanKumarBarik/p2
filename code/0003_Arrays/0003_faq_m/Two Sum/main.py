class Solution:
    def twoSum(self, nums, target):
        m = {}
        res = []
        for i in range(len(nums)):
            curr = nums[i]
            req = target - curr

            if req in m:
                res.append(i)
                res.append(m[req])
                return res 
            m[curr] = i
        return res
                
        
s  = Solution()
nums = [2,7,11,15]
target = 9
result = s.twoSum(nums, target)
print(result)       