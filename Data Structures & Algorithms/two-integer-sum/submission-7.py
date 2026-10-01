class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in m:
                return [m[diff], i]
            m[n] = i