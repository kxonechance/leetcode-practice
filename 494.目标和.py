#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt_0 = len([x for x in nums if x == 0])
        nums = [x for x in nums if x != 0]
        if len(nums) == 0:
            if target == 0:
                return pow(2, cnt_0)
            else:
                return 0
        # pos + neg = sum
        # pos - neg = target
        # pos = (sum + target) // 2
        if sum(nums) + target < 0:
            return 0
        if (sum(nums) + target) % 2 != 0:
            return 0
        pos = (sum(nums) + target) // 2
        
        dp = [[0] * len(nums) for x in range(pos + 1)]

        # base
        for i in range(len(nums)):
            dp[0][i] = 1
        for i in range(1, pos + 1):
            if i == nums[0]:
                dp[i][0] = 1
        # dp
        for i in range(1, pos + 1):
            for j in range(1, len(nums)):
                if i >= nums[j]:
                    dp[i][j] = dp[i][j] + dp[i - nums[j]][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j] + dp[i][j - 1]
        
        return dp[-1][-1] * pow(2, cnt_0)
# @lc code=end 

