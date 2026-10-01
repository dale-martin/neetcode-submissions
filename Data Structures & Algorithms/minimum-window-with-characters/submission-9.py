class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        for char in t:
            counts[char] += 1
        
        need = len(counts)
        l = 0
        bestMatch = [-1, -1]
        bestMatchLen = float('inf')

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] -= 1
                if counts[s[r]] == 0:
                    need -= 1

                    while need == 0:
                        if (r - l + 1) < bestMatchLen:
                            bestMatch = [l, r]
                            bestMatchLen = r - l + 1
                        
                        if s[l] in counts:
                            counts[s[l]] += 1
                            if counts[s[l]] > 0:
                                need += 1
                        l += 1
        
        return s[bestMatch[0] : bestMatch[1] + 1] if bestMatchLen != float('inf') else ''