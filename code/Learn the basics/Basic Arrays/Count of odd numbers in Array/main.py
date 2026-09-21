class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count = 0
        for i in arr:
            if i%2!=0:
                count+=1
        return count
    
s = Solution()
arr = [1, 2, 3, 4, 5]
print(f"Count of odd numbers in the array is: {s.countOdd(arr, len(arr))}")