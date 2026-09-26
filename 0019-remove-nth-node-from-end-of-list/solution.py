# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cur is current position, reqnode is requested node to be removed,
        # and breqnode is the node before the reqnode
        cur = reqnode = breqnode = head
        
        # advance cur pointer n times forward, request node (reqnode) will be n nodes behind
        for i in range(n):
            cur = cur.next

        if cur is None: # edge case for when the head of the list is to be removed
            return head.next
            # you could remove this if condition if you give the head a predecessor node
            # so its treated like all the other nodes: prednode = ListNode(0, head)
        
        # while cur node is not at end of list, advance it and the reqnode
        # before the requested node (breqnode) is saved so we can perform the link once
        # breqnode is removed from the list
        while cur is not None:
            cur = cur.next
            breqnode = reqnode
            reqnode = reqnode.next
        
        breqnode.next = reqnode.next
        
        return head



