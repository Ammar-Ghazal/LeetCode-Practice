# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(n)
        # Space complexity: O(1)

        # Initialize LL we want to return, and a cur ptr to keep track of current location
        head = ListNode()
        cur = head

        # while both lists are non empty:
        while list1 and list2:
            # if list1's value is smaller, put it in merged list
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            # if list2's value is bigger/equal, put it in merged list
            else:
                cur.next = list2
                list2 = list2.next

            # update current pointer so we dont overwrite what we entered in the next iteration
            cur = cur.next
        
        # plug in the rest of the list once the other list runs out
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        
        return head.next

