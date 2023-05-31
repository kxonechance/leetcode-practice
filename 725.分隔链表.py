#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_list_length(head):
            cnt = 0
            curr = head
            while curr:
                cnt += 1
                curr = curr.next
            return cnt

        list_length = get_list_length(head)

        res = []

        if list_length <= k:
            p = head
            for i in range(k):
                if not p:
                    res.append(None)
                else:
                    next = p.next
                    p.next = None
                    res.append(p)
                    p = next
            return res

        else:
            part_length = list_length // k
            extra_cnt = list_length % k

            p = head

            for j in range(extra_cnt):
                prev = None
                curr = p
                for m in range(part_length + 1):
                    prev = curr
                    curr = curr.next
                prev.next = None
                res.append(p)
                p = curr

            for j in range(k - extra_cnt):
                prev = None
                curr = p
                for m in range(part_length):
                    prev = curr
                    curr = curr.next
                prev.next = None
                res.append(p)
                p = curr

            return res    
# @lc code=end

