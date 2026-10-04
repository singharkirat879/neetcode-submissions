from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        answer = []
        for num in nums:
            if num not in numDict:
                numDict[num] = numDict.get(num, 1)
            else:
                numDict[num] += 1
        
        for maxi in range(k):
            maxVar = max(numDict, key=numDict.get)
            answer.append(maxVar)
            del numDict[maxVar]
        
        return answer

            