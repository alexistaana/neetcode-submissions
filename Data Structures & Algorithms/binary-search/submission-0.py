class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 # move

            if nums[mid] == target: # if target is same
                return mid
            elif nums[mid] < target: # if target is on left branch
                left = mid + 1
            else:
                right = mid - 1 # if target is on right branch

        return -1