class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n - 2, -1, -1):
            temp = temperatures[i]
            offset = 1
            while temp >= temperatures[i + offset]:
                if result[i + offset] == 0:
                    offset = 0
                    break
                offset += result[i + offset]
            result[i] = offset

        return result
