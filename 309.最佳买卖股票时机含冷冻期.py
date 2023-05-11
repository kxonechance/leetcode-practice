#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 未交易持有，未交易不持有，交易持有，交易不持有
        dp = [[0, 0, 0, 0] for x in range(len(prices))]
        # base
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        dp[0][3] = 0
        # dp
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][1] - prices[i]
            dp[i][3] = max(dp[i - 1][0], dp[i - 1][2]) + prices[i]
        return max(dp[-1])
# @lc code=end

