class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s in anagrams:
                anagrams[s].append(word)
            else:
                anagrams[s] = [word]
                
        return list(anagrams.values())