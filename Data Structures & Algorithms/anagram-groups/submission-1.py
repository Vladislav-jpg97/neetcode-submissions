class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word_in_strs = "".join(sorted(word))
            anagrams[sorted_word_in_strs] = anagrams.get(sorted_word_in_strs, []) + [word]
            
        return list(anagrams.values())
