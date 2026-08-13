class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for i in nums:
            if i in has:
                return True
            else:
                has.add(i)

        return False