class Solution:
    def isomorphicString(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            # s -> t
            if a in s_map and s_map[a] != b:
                return False

            # t -> s
            if b in t_map and t_map[b] != a:
                return False

            s_map[a] = b
            t_map[b] = a

        return True
            
            
sol = Solution()
s ="foo"
t ="bar"
print(sol.isomorphicString(s, t))