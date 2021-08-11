# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    the solution is to create 2 linked list, one contains smaller nodes only
    while the other contains larger element only.
    then link the 2 lists together

    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        ldummy, rdummy = ListNode(), ListNode()
        lhead, rhead = ldummy, rdummy

        while head is not None:
            if head.val < x:
                lhead.next = head
                lhead = lhead.next
            else:
                rhead.next = head
                rhead = rhead.next
            head = head.next
        rhead.next = None
        lhead.next = rdummy.next

        return ldummy.next
