#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for x in range(len(coins))]
        # base
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
        # dp
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[i][j] = dp[i][j] + dp[i - 1][j] + dp[i][j - coins[i]]
                else:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
        
        return dp[-1][-1]
# @lc code=end

