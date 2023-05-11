#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        # base
        dp[0] = 1
        # dp
        for i in range(1, len(dp)):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]
# @lc code=end
