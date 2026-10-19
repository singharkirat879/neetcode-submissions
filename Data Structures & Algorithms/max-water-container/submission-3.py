class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxHold = 0

        while i < j:
            low = min(heights[i], heights[j])
            
            if abs(i-j) * low > maxHold:
                maxHold = abs(i-j) * low

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1


        return maxHold    
        