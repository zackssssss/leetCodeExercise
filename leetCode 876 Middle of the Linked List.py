# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        position = head
        while position is not None:
            position = position.next
            n += 1
        n2 = n // 2
        for i in range(n2):
            head = head.next
        return head
