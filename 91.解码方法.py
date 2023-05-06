#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        d = {}
        for i in range(0, 26):
            d[str(i + 1)] = chr(ord('A') + i)

        dp = [0] * len(s)
        # base
        if s[0] in d:
            dp[0] = 1
        # dp
        for i in range(1, len(dp)):
            for j in range(2):
                if s[i - j: i + 1] in d:
                    if i - j == 0:
                        dp[i] = dp[i] + 1
                    else:
                        dp[i] = dp[i] + dp[i - j - 1]
        return dp[-1]
# @lc code=end

