from typing import Optional


class ListNode:
    """
    singly linked list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    merge 2 linked list, there is a skill to use: put a dummy node that points to the first node,
    so that we can directly return dummy.next as result.

    """
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        res = ListNode()
        dummy = res

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        if l1 is not None:
            res.next = l1
        if l2 is not None:
            res.next = l2

        return dummy.next

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        start = res

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        if l1 is not None:
            res.next = l1
        if l2 is not None:
            res.next = l2

        return start
