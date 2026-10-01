class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        x = [[] for _ in range(len(nums))]

        for num, freq in freqs.items():
            x[freq - 1].append(num)
        
        res = []
        for y in reversed(x):
            for z in y:
                res.append(z)
                if len(res) == k:
                    return res
        
        