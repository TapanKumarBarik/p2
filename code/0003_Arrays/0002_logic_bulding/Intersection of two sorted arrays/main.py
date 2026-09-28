class Solution:
    def intersectionArray(self, nums1, nums2):
        m ={}
        for num in nums1:
            if num in m:
                m[num]+=1
            else:
                m[num] =1
        
        res =[]
        for num in nums2:
            if num in m:
                res.append(num)
                m[num]-=1
                if m[num]==0:
                    del m[num]
        return res
    
s = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = s.intersectionArray(nums1, nums2)
print(result)