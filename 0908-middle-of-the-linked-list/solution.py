# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # Time complexity: O(n)
        # Space complexity: O(1)

        fast, slow = head, head

        # if head.next is None: return head
        # elif head.next.next is None: return head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
