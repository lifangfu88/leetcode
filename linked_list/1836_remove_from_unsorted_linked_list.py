# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    2 scans, 1 one keep duplicated val in set
    2 scan remove the duplicated val
    O(n)
    this solution works whether the list is sorted or not
    """
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dup = set()
        seen = set()

        dummy = ListNode

        dummy.next = head

        while head:
            if head.val in seen:
                dup.add(head.val)
            seen.add(head.val)
            head = head.next

        cursor = dummy

        while cursor:
            if not cursor.next:
                break
            if cursor.next.val in dup:
                o = cursor.next
                cursor.next = cursor.next.next
                o.next = None
            else:
                cursor = cursor.next

        return dummy.next
