#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for x in range(len(coins))]
        # base
        for i in range(len(coins)):
            dp[i][0] = 0
        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
        # dp
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i][j - coins[i]] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
# @lc code=end

