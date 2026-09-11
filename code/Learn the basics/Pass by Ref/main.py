class Solution:
    def reverse(self, arr: list) -> None:
        i = 0
        j = len(arr)-1
        while i<j:
            self.swap(i,j,arr)
            i+=1
            j-=1
        return arr
    def swap(self,i,j ,arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp



s = Solution()
arr_lists = [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]]
for arr in arr_lists:
    print(s.reverse(arr))