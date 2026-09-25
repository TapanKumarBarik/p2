class Solution:
    def mergeSort(self, nums):

        n = len(nums)
        # for lenght 1 or empty array
        if n<=1:
            return nums
        
        mid = n//2

        left_array = self.mergeSort(nums[:mid])
        right_array = self.mergeSort(nums[mid:])
        return self.merge(left_array, right_array)
        
    
    def merge(self, left_array,right_array):
        n = len(left_array)
        m = len(right_array)
        i = 0
        j = 0
        res =[]

        while i<n and j<m:
            if left_array[i]<=right_array[j]:
                res.append(left_array[i])
                i+=1
            else:
                res.append(right_array[j])
                j+=1
        while i<n:
            res.append(left_array[i])
            i+=1
        while j<m:
            res.append(right_array[j])
            j+=1
        return res

            
            
solution = Solution()
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = solution.mergeSort(nums)