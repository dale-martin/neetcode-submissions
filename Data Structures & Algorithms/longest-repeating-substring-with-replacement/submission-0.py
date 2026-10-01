class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxCount = 0
        l = 0
        maxSize = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxCount = max(maxCount, counts[s[r]])

            while (r - l + 1) - maxCount > k:
                counts[s[l]] -= 1
                l += 1
            
            maxSize = max(maxSize, r - l + 1)

        return maxSize