class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        bestK = r

        while l <= r:
            m = l + (r - l) // 2
            time = sum(-(-pile // m) for pile in piles)
            if time <= h:
                bestK = m
                r = m - 1
            else:
                l = m + 1
        
        return bestK