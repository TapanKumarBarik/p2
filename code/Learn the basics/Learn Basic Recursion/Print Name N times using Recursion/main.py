class Solution:
    def printName(self,name:str, n:int):
        if n==0:
            return
        print(n, name)
        self.printName(name, n-1)

s = Solution()
s.printName("John", 500)