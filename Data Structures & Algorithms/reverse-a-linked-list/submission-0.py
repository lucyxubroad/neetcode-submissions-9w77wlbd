# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0 -> 1 -> 2 -> 3

curr = 0
next = 1

save = next.next
next.next = curr
curr = save

1 -> 0

before you set next of 1 to 0, save the 2 


'''

class Solution:

    def reverse(self, prev, head, next):
        if next is None:
            return head 
    
        head.next = prev
        next_next = next.next
        next.next = head

        return self.reverse(head, next, next_next)



    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        return self.reverse(None, head, head.next)
