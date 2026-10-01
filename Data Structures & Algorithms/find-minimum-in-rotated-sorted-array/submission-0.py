class Solution:
    def findMin(self, nums: List[int]) -> int:
        bestMin = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < bestMin:
                r = m - 1
                bestMin = nums[m]
            else:
                l = m + 1
        
        return bestMin