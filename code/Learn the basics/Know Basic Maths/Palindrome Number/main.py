class Solution:
    def isPalindrome(self, n):
        if n<10:
            return True
        num = str(n)
        i = 0
        j = len(num)-1
        while i<j:
            if num[i]!=num[j]:
                return False
            i+=1
            j-=1
        return True
    
s = Solution()
n_list = [121, 12321, 123, 45654, 98789]
for n in n_list:
    print(s.isPalindrome(n))
    print("----------")