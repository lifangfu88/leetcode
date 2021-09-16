from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        # 2 dummy nodes to make it at least 3 element
        dummy = ListNode(-1)
        dummy.next = head
        before_dum = ListNode(-2)
        before_dum.next = dummy

        # get list length
        leng = 0
        while head:
            leng += 1
            head = head.next

        if n > leng:
            return None
        # target position considering 2 dummy nodes
        target = leng - n + 2

        head = dummy
        while target > 2:
            head = head.next
            target -= 1

        before = head
        tar = head.next
        if not head.next:
            after = None
        else:
            after = head.next.next

        if tar:
            tar.next = None
        before.next = after

        return dummy.next
