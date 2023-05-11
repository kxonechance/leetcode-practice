#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        # base
        if s[0] in wordDict:
            dp[0] = True
        # dp
        for i in range(1, len(s)):
            for j in range(i + 1):
                if s[j: i + 1] in wordDict:
                    if j == 0:
                        dp[i] = True
                    else:
                        dp[i] = dp[i] or dp[j - 1]
        return dp[-1]
# @lc code=end

