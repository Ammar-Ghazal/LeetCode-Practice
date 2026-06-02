# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False

        # Initial Impelementation
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # visited = set()
        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        
        # return False
