#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        
        # 用到第i个数时，能否满足凑成j的情况
        dp = [[False] * len(nums) for x in range(target + 1)]
        # base
        for i in range(len(nums)):
            dp[0][i] = True
        for i in range(1, target + 1):
            if i == nums[0]:
                dp[i][0] = True
        # dp
        for i in range(1, target + 1):
            for j in range(1, len(nums)):
                if i >= nums[j]:
                    dp[i][j] = dp[i][j] or dp[i - nums[j]][j - 1] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[-1][-1]
# @lc code=end

