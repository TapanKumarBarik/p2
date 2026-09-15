class Solution:
    def pattern15(self, n):
        for i in range(n):
            for j in range(n-i):
                print(chr(ord("A")+j) , end= "")
            print()

s = Solution()
n_list = [22,23,24,25,26]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern15(n)
    print()