class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord('a')] += 1
        for char in t:
            chars[ord(char) - ord('a')] -= 1
        for char in chars:
            if char != 0: return False

        return True
