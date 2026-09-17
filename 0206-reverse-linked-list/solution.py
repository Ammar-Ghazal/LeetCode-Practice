# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, curr: ListNode | None) -> ListNode | None:
        reversed = None

        while curr is not None:
            next_node = curr.next
            curr.next = reversed
            reversed = curr
            curr = next_node

        return reversed
