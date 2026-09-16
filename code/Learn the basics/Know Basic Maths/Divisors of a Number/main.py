class Solution:
    def divisors(self, n):
        res_arr = []
        for i in range(1 ,n+1,1 ):
            if n%i == 0:
                res_arr.append(i)
        return res_arr
    
    
s = Solution()
n_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in n_list:
    print(f"Divisors of {n} are {s.divisors(n)}")