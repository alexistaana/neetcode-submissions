class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            h1[s[i]] = h1.get(s[i], 0) + 1  
            h2[t[i]] = h2.get(t[i], 0) + 1

        return True if h1 == h2 else False