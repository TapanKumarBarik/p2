class Solution:
    def reverse(self, arr: list, n: int) -> None:
        self.reverse_array(arr, 0,n-1)
        return arr
    def reverse_array(self, arr,start, end):
        if start>=end:
            return
        self.swap(arr, start,end)
        self.reverse_array(arr, start+1, end-1)
    def swap(self, arr, start, end):
        temp = arr[end]
        arr[end] = arr[start]
        arr[start] = temp
    


s = Solution()
arr_list = [[1,2,3,4,5], [1,2,3,4], [1], [], [1,2]]
for arr in arr_list:
    print(s.reverse(arr, len(arr)))
    print("-----------------------------")
    