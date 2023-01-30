# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        while(True):
            if(l1 != None):
                str1 += str(l1.val)
                l1 = l1.next
            if(l2 != None):
                str2 += str(l2.val)
                l2 = l2.next
            elif(l1 == None and l2 == None):
                break

        num1 = int(str1[::-1])
        num2 = int(str2[::-1])
        totalnum = (str(num1 + num2))[::-1];
        length = len(totalnum);
        firsttime = 0
        tail = head = ListNode(totalnum[0])
        for char in totalnum:
            if(firsttime == 0):
                firsttime += 1
                pass
            else:
                tail.next = ListNode(char)
                tail = tail.next
    
        print(f"totalnum is {totalnum}")

        return head




