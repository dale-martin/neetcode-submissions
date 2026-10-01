class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [c.lower() for c in s if c.isalnum()]
        if x == list(reversed(x)):
            return True
        return False