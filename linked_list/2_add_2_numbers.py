# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/add-two-numbers/
    2 solutions:
     1. add based on the linked list nodes, need to take care of incremental
     2. convert to int, sum, and convert back

    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        v1 = self.get_val(l1)
        v2 = self.get_val(l2)
        if v1 == 0:
            return l2
        if v2 == 0:
            return l1

        return self.build_list(v1 + v2)

    def build_list(self, v):
        dummy, res = ListNode(-1), ListNode(0)
        dummy.next = res

        while v >= 1:
            n_v = v // 10
            c_v = v - n_v * 10
            res.next = ListNode(c_v)

            v = n_v
            res = res.next
        return dummy.next.next

    def get_val(self, l):
        res = 0
        i = 0
        while l:
            res += l.val * 10**i
            l = l.next
            i += 1
        return res
