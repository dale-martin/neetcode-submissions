from bisect import bisect

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.m[key]
        i = bisect(values, timestamp, key=lambda pair: pair[0]) - 1
        return values[i][1] if i >= 0 else ''
