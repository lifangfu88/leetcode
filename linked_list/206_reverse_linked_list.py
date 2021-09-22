from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = []

        while head:
            res.append(head.val)
            head = head.next

        dummy = ListNode(-1)
        root = dummy
        for i in range(len(res)-1, -1, -1):
            dummy.next = ListNode(res[i])
            dummy = dummy.next

        return root.next
