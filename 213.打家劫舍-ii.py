#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # dp1，抢第一个
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        for i in range(2, len(dp1)):
            if i == len(dp1) - 1:
                dp1[i] = dp1[i - 1]
            else:
                dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        # dp2，不抢第一个
        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        for i in range(2, len(dp2)):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        return max(dp1[-1], dp2[-1])
# @lc code=end

