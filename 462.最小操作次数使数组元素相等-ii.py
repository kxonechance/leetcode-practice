#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最小操作次数使数组元素相等 II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = sorted(nums)[len(nums) // 2]
        return sum([abs(x - mid) for x in nums])
# @lc code=end

