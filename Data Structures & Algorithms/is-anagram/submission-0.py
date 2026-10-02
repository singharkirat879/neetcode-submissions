class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:
            sDict = {}
            tDict = {}
            for letter in s:
                if(letter not in sDict):
                    sDict[letter]=sDict.get(letter, 1)
                else:
                    sDict[letter] += 1
            
            for letter in t:
                if(letter not in tDict):
                    tDict[letter] = tDict.get(letter, 1)
                else:
                    tDict[letter]+=1

            if(sDict == tDict):
                return True
            else:
                return False