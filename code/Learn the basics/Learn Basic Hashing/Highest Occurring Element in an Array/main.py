class Solution:
    def mostFrequentElement(self, nums):
        map_data={}
        for i in nums:
            if i in map_data:
                map_data[i]+=1
            else:
                map_data[i]=1

        max_freq=0
        for key , value in map_data.items():
            max_freq = max(max_freq, value)

        possible_res=[]
        for key , value in map_data.items():
            if value==max_freq:
                possible_res.append(key)
        
        min_res=possible_res[0]

        for i in possible_res:
            min_res = min(min_res, i)

        return min_res




s = Solution()
nums_list = [[1, 2, 2, 3, 3, 3], [4, 4, 4, 4], [5, 6, 7, 8, 9], [10, 10, 10, 10, 10]]
for nums in nums_list:
    print(f"Highest occurring element in {nums} is: {s.mostFrequentElement(nums)}")
     