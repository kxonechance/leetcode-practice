#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        while p2:
            while p2 and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p2
            if p2:
                p2.next
        return head
# @lc code=end

