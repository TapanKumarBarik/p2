class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end ="")
            print()
            
            
s = Solution()
n_list = [5, 3, 7]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern2(n)
    print()