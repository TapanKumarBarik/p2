class Solution:
    def mergeSort(self, nums):
        n = len(nums)
        self.merge_sort_helper(nums,0, n-1)
        return nums
    def merge_sort_helper(self,nums, start, end ):
        if start>=end:
            return 
        
        mid = (start+end)//2

        self.merge_sort_helper(nums, start, mid)
        self.merge_sort_helper(nums, mid+1, end)
        self.merge(nums,start, mid, end)
    
    def merge(self, nums, start, mid ,end):
        temp =[]
        low = start
        right = mid+1
        while start<=mid and right<=end:
            if nums[start]<=nums[right]:
                temp.append(nums[start])
                start+=1
            else:
                temp.append(nums[right])
                right+=1

        while start<=mid:
            temp.append(nums[start])
            start+=1
        while right<=end:
            temp.append(nums[right])
            right+=1

        for i in range(low, end+1):
            nums[i]= temp[i-low]
            
            
solution = Solution()
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = solution.mergeSort(nums)