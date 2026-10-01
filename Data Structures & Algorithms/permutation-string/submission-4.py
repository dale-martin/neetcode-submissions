class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counts = defaultdict(int)

        for char in s1:
            counts[char] += 1

        for i in range(len(s1)):
            counts[s2[i]] -= 1
        
        for r in range(len(s1), len(s2)):
            if all(val == 0 for val in counts.values()):
                return True

            counts[s2[r - len(s1)]] += 1
            counts[s2[r]] -= 1
        
        if all(val == 0 for val in counts.values()):
            return True
            
        return False