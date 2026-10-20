class Solution:
    def trap(self, height: list[int]) -> int:
        bldgs = len(height)
        if bldgs == 0:
            return 0

        leftMax = [0] * bldgs
        rightMax = [0] * bldgs

        leftMax[0] = height[0]

        for i in range(1, bldgs):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[bldgs - 1] = height[bldgs - 1]

        for i in range( bldgs- 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        hold = 0

        for l in range(bldgs):
            hold += min(leftMax[l], rightMax[l]) - height[l]

        return hold
