class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}
        for i in range(len(s)):
            h1[s[i]] = h1.get(s[i], 0) + 1  
        
        for i in range(len(t)):
            h2[t[i]] = h2.get(t[i], 0) + 1

        return True if h1 == h2 else False