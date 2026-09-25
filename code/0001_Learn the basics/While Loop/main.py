class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        count_till = 1
        
        if d == 0:
            num_to_add = 10
        else:
            num_to_add =d
        sum = num_to_add
        while count_till<50:
            num_to_add = num_to_add+10
            sum+=num_to_add
            count_till+=1
        return sum





s = Solution()
d_array = [0, 1, 2, 3, 4, 5]
for d in d_array:
    print(s.whileLoop(d))
    print("----------")