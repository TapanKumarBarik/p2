class Solution:
    def rearrangeArray(self, nums):
        first_positive =0
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]>0:
                first_positive =i 
                break
            i+=1

        first_negetive =0
        i =0
        while i<n:
            if nums[i]<0:
                first_negetive =i 
                break
            i+=1

        res =[]

    
        while first_positive<n and first_negetive<n:
            if nums[first_positive]<0:
                first_positive+=1
                continue
            elif nums[first_negetive]>0:
                first_negetive+=1
                continue
            res.append(nums[first_positive])
            res.append(nums[first_negetive])
            first_positive+=1
            first_negetive+=1
        
        return res



        
s = Solution()
nums = [3, 1, -2, -5, 2, -4]
result = s.rearrangeArray(nums)
print(result) # Output: [3, -2, 1, -5, 2, -4]