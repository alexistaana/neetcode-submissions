class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        has = dict()

        for i,j in zip(s,t):
            has[i] = has.get(i, 0) + 1
            has[j] = has.get(j, 0) - 1


        if all(value == 0 for value in has.values()):
            return True

        return False
