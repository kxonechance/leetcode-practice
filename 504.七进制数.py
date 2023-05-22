#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = True
        if num < 0:
            flag = False
        num = abs(num)

        res = []
        while num > 0:
            shang = num // 7
            yu = num % 7
            res.insert(0, str(yu))
            num = shang

        if not flag:
            res.insert(0, '-')

        return ''.join(res)
# @lc code=end

