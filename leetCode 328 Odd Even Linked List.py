# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        if head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead

        return head
