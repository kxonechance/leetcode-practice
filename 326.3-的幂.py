#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return n == 1
# @lc code=end

