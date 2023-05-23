#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pa = len(a) - 1
        pb = len(b) - 1
        res = []
        flag = False
        while pa >= 0 and pb >= 0:
            cha = a[pa]
            chb = b[pb]
            if not flag:
                if cha == '0' and chb == '0':
                    res.insert(0, '0')
                elif cha == '0' and chb == '1':
                    res.insert(0, '1')
                elif cha == '1' and chb == '0':
                    res.insert(0, '1')
                else:
                    res.insert(0, '0')
                    flag = True
            else:
                if cha == '0' and chb == '0':
                    res.insert(0, '1')
                    flag = False
                elif cha == '0' and chb == '1':
                    res.insert(0, '0')
                    flag = True
                elif cha == '1' and chb == '0':
                    res.insert(0, '0')
                    flag = True
                else:
                    res.insert(0, '1')
                    flag = True
            pa -= 1
            pb -= 1

        if pa >= 0:
            while pa >= 0:
                cha = a[pa]
                if flag:    
                    if cha == '0':
                        res.insert(0, '1')
                        flag = False
                    else:
                        res.insert(0, '0')
                        flag = True
                else:
                    if cha == '0':
                        res.insert(0, '0')
                    else:
                        res.insert(0, '1')
                pa -= 1


        if pb >= 0:
            while pb >= 0:
                chb = b[pb]
                if flag:    
                    if chb == '0':
                        res.insert(0, '1')
                        flag = False
                    else:
                        res.insert(0, '0')
                        flag = True
                else:
                    if chb == '0':
                        res.insert(0, '0')
                    else:
                        res.insert(0, '1')
                pb -= 1

        if flag:
            res.insert(0, '1')

        return ''.join(res)
# @lc code=end

