from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in anagram:
                anagram[s].append(strs[i])
            else:
                anagram[s] = [strs[i]]
        
        return list(anagram.values())

