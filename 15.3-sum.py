#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

import time
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       start = time.time()
       trips = []
       seen = {}

       for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i == j:
                    break
                for k in range(j + 1, len(nums)):
                   if i == k or j == k:
                       break

                   inorder = sorted([nums[i], nums[j], nums[k]])
                   if seen.get(f'{inorder}') != None:
                       break
                
                   if sum(inorder) == 0:
                       trips.append(inorder)
                       seen[f'{inorder}'] = True

       end_time = time.time() - start 
       return trips
# @lc code=end

f = Solution()
nums = [-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]
f.threeSum(nums=nums)