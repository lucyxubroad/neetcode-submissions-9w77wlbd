# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len_list = 0
        iter_node = head

        while iter_node is not None:
            len_list += 1
            iter_node = iter_node.next

        remove_index = len_list - n
        if remove_index == 0:
            return head.next

        iter_node = head
        for i in range(0, remove_index-1):
            iter_node = iter_node.next 
        
        node_before_remove_node = iter_node
        node_to_remove = iter_node.next
        node_after_remove = iter_node.next.next

        iter_node.next = None
        node_before_remove_node.next = node_after_remove

        return head
        
