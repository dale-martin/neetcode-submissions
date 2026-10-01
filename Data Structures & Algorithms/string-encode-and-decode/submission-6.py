class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) > 0:
            l, _, s = s.partition('#')
            res.append(s[:int(l)])
            s = s[int(l):]
        return res