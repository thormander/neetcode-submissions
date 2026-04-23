# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode()
        newP = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                newP.next = ListNode(l1.val)
                newP = newP.next
                l1 = l1.next
            else:
                newP.next = ListNode(l2.val)
                newP = newP.next
                l2 = l2.next

        #  finsh tail end that hasnt been fully incremented through
        while l1:
            newP.next = ListNode(l1.val)
            newP = newP.next
            l1 = l1.next            
            
        while l2:
            newP.next = ListNode(l2.val)
            newP = newP.next
            l2 = l2.next

        return dummy.next              



'''
pointer at each head

use a new linked list

compare val between
    - take whichever is smaller/equal and aadd to new

at the end, need to check if one or the other not finished
and just add to end of our list
'''