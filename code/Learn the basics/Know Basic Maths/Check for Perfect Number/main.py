class Solution:
    def isPerfect(self, n: int) -> bool:
        sum =0
        for i in range(1,(n//2)+1):
            if n%i == 0:
                sum+=i
        return sum == n
    
    
s = Solution()
n_list = [6, 28, 496, 8128, 33550336, 12, 97, 100]
for n in n_list:
    if s.isPerfect(n):
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")