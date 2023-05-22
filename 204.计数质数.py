#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        nums = [True] * n
        for i in range(2, n):
            if nums[i]:
                for j in range(i, n):
                    if i * j < n:
                        nums[i * j] = False
                    else:
                        break
        res = 0
        for i in range(2, n):
            if nums[i] == True:
                res += 1

        return res
# @lc code=end

