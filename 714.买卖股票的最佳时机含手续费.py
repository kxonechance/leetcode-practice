#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 持有，交易不持有，未交易不持有
        dp = [[0, 0, 0] for x in range(len(prices))]
        # base
        dp[0][0] = -fee - prices[0]
        dp[0][1] = -fee
        dp[0][2] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(max(dp[i - 1][1], dp[i - 1][2]) - prices[i] - fee, dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1])
# @lc code=end

