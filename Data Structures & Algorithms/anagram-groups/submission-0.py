class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))

            # last few code can be written as 
            # groups.setdefault(key, []).append(word)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
