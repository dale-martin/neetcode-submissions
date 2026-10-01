class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        cutoff = sorted(list(freqs.values()), reverse=True)[k-1]
        top = []
        for key, val in freqs.items():
            if val >= cutoff:
                top.append(key)
        
        return top