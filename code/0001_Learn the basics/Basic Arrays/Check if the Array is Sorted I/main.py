class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(1, n):
            if arr[i-1]>arr[i]:
                return False
        return True
        
        
s = Solution()
arr = [1, 2, 3, 4, 5]
if s.arraySortedOrNot(arr, len(arr)):
    print("The array is sorted.")