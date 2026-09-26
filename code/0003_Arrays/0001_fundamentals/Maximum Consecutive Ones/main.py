class Solution:
    def findMaxConsecutiveOnes(self, nums):

        max_count = 0
        temp = 0
        for i in nums:
            if i == 0:
                max_count = max(max_count,temp )
                temp = 0
            else:
                temp+=1
        return max(max_count,temp )

        
s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))