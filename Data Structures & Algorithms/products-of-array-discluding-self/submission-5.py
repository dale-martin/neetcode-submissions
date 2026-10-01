class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        z_count = 0
        for num in nums:
            if num == 0:
                z_count += 1
            else:
                total *= num
            
        if z_count > 1:
            return [0] * len(nums)

        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if z_count: output[i] = 0 if num else total
            else: output[i] = total // num
        
        return output