# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        # place a gap of n between l and r pointers
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # now increase both pointers till we reach the end
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummyNode.next
