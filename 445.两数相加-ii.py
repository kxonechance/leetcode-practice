#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = ListNode(-1)
        p = dummy
        flag = False

        while l1 and l2:
            val = l1.val + l2.val
            if flag:
                val += 1
                flag = False
            if val >= 10:
                val -= 10
                flag = True
            l1 = l1.next
            l2 = l2.next
            p.next = ListNode(val)
            p = p.next

        if l1:
            while l1:
                val = l1.val
                if flag:
                    val += 1
                    flag = False
                if val >= 10:
                    val -= 10
                    flag = True
                l1 = l1.next
                p.next = ListNode(val)
                p = p.next

        if l2:
            while l2:
                val = l2.val
                if flag:
                    val += 1
                    flag = False
                if val >= 10:
                    val -= 10
                    flag = True
                l2 = l2.next
                p.next = ListNode(val)
                p = p.next

        if flag:
            p.next = ListNode(1)  
        
        return reverse(dummy.next)

# @lc code=end

