# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        curr = head
        next = head
        for i in range(m - 1):
            prev = curr
            curr = curr.next

        prev2 = prev
        curr2 = curr

        for i in range(m, n + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        if prev2 is None:
            head = prev
        else:
            prev2.next = prev
        curr2.next = curr

        return head
