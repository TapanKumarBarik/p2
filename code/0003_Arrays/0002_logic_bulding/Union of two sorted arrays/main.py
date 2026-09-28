class Solution:
    def unionArray(self, nums1, nums2):
        s = set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            s.add(num)
        return sorted(s)




s = Solution()
nums1 = [1, 2, 4, 5, 6]
nums2 = [2, 3, 5, 7]
result = s.unionArray(nums1, nums2)