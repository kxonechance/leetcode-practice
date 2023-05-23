#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 1
        while pow(5, i) <= n:
            res = res + n // pow(5, i)
            i += 1
        return res
# @lc code=end

