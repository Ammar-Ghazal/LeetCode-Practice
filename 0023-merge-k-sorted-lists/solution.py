# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Time complexity: O(nlogn), n log n b/c sorting requires nlogn
        # Space complexity: O(n), for the new linked list
        vals = []
        curr = temp = ListNode(0)

        # traverse current linked lists, and add the values to vals
        for i in range(len(lists)):
            cur = lists[i]
            while cur is not None:
                vals.append(cur.val)
                cur = cur.next
        
        vals.sort() # sorting vals
        
        # create new linked list and insert sorted values
        for num in vals:
            curr.next = ListNode(num)
            curr = curr.next
        
        return temp.next
