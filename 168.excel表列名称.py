#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def num2char(x):
            return chr(x + ord('A'))

        res = []
        while columnNumber > 0:
            shang = (columnNumber - 1) // 26
            yu = (columnNumber - 1) % 26
            res.insert(0, num2char(yu))
            columnNumber = shang

        return ''.join(res)
# @lc code=end

