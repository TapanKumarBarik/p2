class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        res_arr = []
        map_res={}

        for n in nums:
            if n in map_res:
                map_res[n] =map_res[n]+1
            else:
                map_res[n]=1
        for key, value in map_res.items():
            temp_arr=[]
            temp_arr.append(key)
            temp_arr.append(value)
            res_arr.append(temp_arr)
        return res_arr


s = Solution()
nums_list = [[1, 2, 2, 3, 3, 3], [4, 4, 4, 4], [5, 6, 7, 8, 9], [10, 10, 10, 10, 10]]
for nums in nums_list:
    print(f"Frequencies of {nums} are: {s.countFrequencies(nums)}")