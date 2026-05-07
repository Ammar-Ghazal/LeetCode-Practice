# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n+m) time complexity (list1 is n, list2 is m), and O(1) space complexity (only creating headptr and curr)
        headptr = ListNode()
        curr = headptr

        # while both lists are not empty:
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # be sure to look at the node we just entered in curr.next (list1/list2)
            curr = curr.next

        # if either list becomes empty, then set the rest of the list to be the non empty one
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return headptr.next

