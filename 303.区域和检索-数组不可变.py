#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0] * len(nums)
        # base
        self.dp[0] = nums[0]
        # dp
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.dp[right]
        else:
            return self.dp[right] - self.dp[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

