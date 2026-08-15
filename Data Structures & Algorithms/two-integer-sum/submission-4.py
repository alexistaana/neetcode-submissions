class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            if target - nums[i] in hash.keys():
                return [hash[target - nums[i]], i]
            
            hash[nums[i]] = i
        
        return [0,0]

