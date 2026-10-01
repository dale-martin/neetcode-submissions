class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        maxLen = 0

        for char in s:
            if char in substr:
                substr = substr.split(char)[1]
            substr += char

            maxLen = max(maxLen, len(substr))
        
        return maxLen