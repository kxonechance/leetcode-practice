#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        dp = [[0] * len(text2) for x in range(len(text1))]
        # base
        min_index = -1
        for i in range(len(text1)):
            if text2[0] == text1[i]:
                min_index = i
                break
        if min_index != -1:
            for i in range(min_index, len(text1)):
                dp[i][0] = 1
        
        min_index = -1
        for i in range(len(text2)):
            if text1[0] == text2[i]:
                min_index = i
                break
        if min_index != -1:
            for i in range(min_index, len(text2)):
                dp[0][i] = 1
        
        # dp
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
# @lc code=end

