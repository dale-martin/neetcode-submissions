class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxSize = 0
        stack = []
        n = len(heights)

        for i in range(n + 1):
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxSize = max(maxSize, height * width)
            stack.append(i)
        
        return maxSize