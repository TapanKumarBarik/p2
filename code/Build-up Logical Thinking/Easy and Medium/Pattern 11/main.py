class Solution:
    def pattern11(self, n):
        for i in range(n):
            
            for j in range(i+1):
                if i%2!=0:
                    print(j & 1 , end=" ")
                else:
                    if j%2 ==0:
                        print("1" ,end=" ")
                    else:
                        print("0",end=" ")
            print()
            
            
sol = Solution()
n_list = [5, 3, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern11(n)
    print()