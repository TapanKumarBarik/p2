class Solution:
    def frequencySort(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        return sorted(freq, key=lambda x: (-freq[x], x))
    
    
s = "tree"
solution = Solution()
result = solution.frequencySort(s)
print(result)  # Output: ['e', 'e', 'r', 't']