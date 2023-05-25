#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(left)):
            left[i] = nums[i - 1] * left[i - 1]
        for i in range(len(right) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res
# @lc code=end

