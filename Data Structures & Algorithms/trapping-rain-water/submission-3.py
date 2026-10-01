class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        area = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                if height[l] < maxL:
                    area += maxL - height[l]
                else:
                    maxL = height[l]
            else:
                r -= 1
                if height[r] < maxR:
                    area += maxR - height[r]
                else:
                    maxR = height[r]
        
        return area