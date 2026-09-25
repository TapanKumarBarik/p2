class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        return self.check_palindrome(s,0,len(s)-1)
    def check_palindrome(self,s,start,end):
        if start>=end:
            return True
        
        if s[start] != s[end]:
            return False
        return self.check_palindrome(s, start+1,end-1)
    
s = Solution()
s_list = ["racecar", "hello", "madam", "python", "level"]
for string in s_list:
    if s.palindromeCheck(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")