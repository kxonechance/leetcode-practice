#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 最小的两个负数和最大的正数 或者 三个最大的正数
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
# @lc code=end

