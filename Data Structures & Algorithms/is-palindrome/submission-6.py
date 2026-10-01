class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [c.lower() for c in s if c.isalnum()]
        print(x, list(reversed(x)))
        if x == list(reversed(x)):
            return True
        return False