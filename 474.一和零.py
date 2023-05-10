#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def get_cnt(s):
            cnt_0 = 0
            cnt_1 = 0
            for c in s:
                if c == '0':
                    cnt_0 += 1
                else:
                    cnt_1 += 1
            return [cnt_0, cnt_1]

        dp = [[0] * (n + 1) for x in range(m + 1)]
        # dp
        for s in strs:
            cnt0, cnt1 = get_cnt(s)
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[-1][-1]
# @lc code=end

