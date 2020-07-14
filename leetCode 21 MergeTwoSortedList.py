# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode()

        dummy = curr

        while (l1.next != None) and (l2.next != None):
            if l1.val < l2.val:
                curr.next = l1.val
                l1 = l1.next
            else:
                curr.next = l2.val
                l2 = l2.next
            curr = curr.next

        if (l1.next != None):
            curr.next = l1
        if (l2.next != None):
            curr.next = l2

        return dummy.next
