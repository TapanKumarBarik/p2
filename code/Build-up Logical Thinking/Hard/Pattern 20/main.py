class Solution:
    def pattern20(self, n):
        for i in range(2*n-1):
            if i<n:
                #increase
                print("*"*(i+1)+" "*(2*n-i-i-2)+"*"*(i+1))
            else:
                #decrease
                print("*"*(2*n-i-1)+" "*(2*(i-n+1))+"*"*(2*n-i-1))
                
s = Solution()
n_list = [5, 6, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern20(n)
    print()