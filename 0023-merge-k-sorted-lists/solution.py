# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        combinedList = [] # where we will combine the linked lists, and sort them
        out = ListNode(0) # will contain the linked list version of combinedList

        for linkedList in lists:
            while linkedList:
                combinedList.append(linkedList.val)
                linkedList = linkedList.next
        
        combinedList.sort()

        temp = out
        for num in combinedList:
            temp.next = ListNode(num)
            temp = temp.next

        # be sure to return the one after the dummy head pointer
        return out.next        
