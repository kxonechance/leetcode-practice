#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 覆盖到第i个数时，最后一个以上升/或者下降结尾时，最长的摆动序列
        up = [1] * len(nums)
        down = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]

        return max(up[-1], down[-1])
# @lc code=end

