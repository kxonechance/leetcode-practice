#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        # base
        dp[0] = 0
        dp[1] = 1
        # dp
        for i in range(2, n + 1):
            for j in range(1, i):
                if j * j <= i:
                    dp[i] = min(dp[i], 1 + dp[i - j * j])
                else:
                    break
        return dp[-1]
# @lc code=end

