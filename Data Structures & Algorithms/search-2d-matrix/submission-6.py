from bisect import bisect_left, bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect_right(matrix, target, key=lambda r: r[0]) - 1
        col = bisect_left(matrix[row], target)
        return True if col < len(matrix[0]) and matrix[row][col] == target else False