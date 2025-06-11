#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
 
        quotient = n 
        rem = 0
 
        while quotient > 0:
            bits += quotient % 2
            quotient = quotient // 2

        return bits
    
# @lc code=end
f = Solution()
f.hammingWeight(6)
