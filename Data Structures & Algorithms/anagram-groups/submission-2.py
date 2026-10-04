from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordList = {}

        for str in strs:
            key = tuple(sorted(Counter(str).items()))
        
            if key not in wordList:
                wordList[key] = []
            
            wordList[key].append(str)

        return list(wordList.values())
        
        