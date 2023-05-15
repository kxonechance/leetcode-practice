#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        # base
        dp[0] = 0
        dp[1] = 0
        # dp
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], i // j + dp[j])
        return dp[-1]
# @lc code=end

