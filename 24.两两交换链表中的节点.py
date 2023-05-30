#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ji = ListNode(-1)
        ou = ListNode(-1)
        pji = ji
        pou = ou
        i = 1
        p = head
        while p:
            if i % 2 == 0:
                pou.next = p
                pou = pou.next
            else:
                pji.next = p
                pji = pji.next
            p = p.next
            i += 1
        pji.next = None
        pou.next = None

        dummy = ListNode(-1)
        dummy.next = None
        pd = dummy

        pji = ji.next
        pou = ou.next

        i = 1

        while pji and pou:
            if i % 2 == 0:
                pd.next = pji
                pji = pji.next
            else:
                pd.next = pou
                pou = pou.next
            pd = pd.next
            i += 1
        
        if pji:
            pd.next = pji
        if pou:
            pd.next = pou

        return dummy.next


# @lc code=end

