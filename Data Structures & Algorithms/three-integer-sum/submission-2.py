class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ansList = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = i+1
            b = len(nums) - 1

            while a < b:
                if nums[i] + nums[a] + nums[b] < 0:
                    a+=1
                elif nums[i] + nums[a] + nums[b] > 0:
                    b-=1
                else:
                    ansList.append([nums[i], nums[a], nums[b]])

                    a+=1
                    b-=1

                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                        
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1

        return ansList

        
                        
        