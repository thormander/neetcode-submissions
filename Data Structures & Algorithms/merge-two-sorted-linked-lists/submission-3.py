# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # pointers for input lists
        top = list1
        bot = list2

        # for result
        placeholder = ListNode()
        final = placeholder

        # merge
        while top and bot:
            
            if top.val <= bot.val:
                final.next = ListNode(top.val,None)
                top = top.next
            else:
                final.next = ListNode(bot.val,None)
                bot = bot.next

            final = final.next
        
        # handle remaining tails
        if top:
            final.next = top
        elif bot:
            final.next = bot

        return placeholder.next

        


'''
2 sorted lists
merge both, return head of new 

result: placeholder node -> node 1 node 2 ...
l1 head
l2 head

plaeholdernode -> 1 
                   |

0  [1,2,4]
        |
0  [1,3,5,8]
          |

take the one with the least, if equal lets just take l1 

take into account if one is still not null
'''