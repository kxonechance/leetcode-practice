#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # 小偷偷到第i个房间，能够偷到的最多的钱
        dp = [-float('inf')] * len(nums)
        # base
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # dp
        for i in range(2, len(dp)):
            # 如果抢了nums[i]，那么nums[i - 1]肯定不能抢
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
# @lc code=end

