#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ji = ListNode(-1)
        ou = ListNode(-1)
        pji = ji
        pou = ou
        i = 1
        p = head
        while p:
            if i % 2 == 1:
                pji.next = p
                pji = pji.next
            else:
                pou.next = p
                pou = pou.next
            p = p.next
            i += 1
        pji.next = ou.next
        pou.next = None

        return ji.next
# @lc code=end

