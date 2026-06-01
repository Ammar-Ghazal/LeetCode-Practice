# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        curr = fast = head

        while fast != None and fast.next != None and fast.next.next != None:
            fast = fast.next.next.next
            curr = curr.next
            if curr == fast:
                return True
        
        return False


        # Initial Implementation:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # visited = set()
        # curr = head

        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        
        # return False
