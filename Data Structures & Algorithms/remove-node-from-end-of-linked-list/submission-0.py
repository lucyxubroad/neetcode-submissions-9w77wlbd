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

        print(remove_index)
        iter_node = head
        for i in range(0, remove_index-1):
            iter_node = iter_node.next 
        
        node_before_remove_node = iter_node
        node_to_remove = iter_node.next
        node_after_remove = iter_node.next.next

        iter_node.next = None
        node_before_remove_node.next = node_after_remove

        return head


        '''
        you need to count the number of elements 
        --> then you know from the front, where you need to stop

        example: len = 4. n=2 means you need

        1 means end 
        2 means second to last 

        (len-1) - n gives you the element before node you need to remove (0 indexed)
            note that this can give you -1 if the list only has one element
        (len-n) gives you element you want to remove (0 indexed)

        1. has a node before & node after
        2. has no node before 


        if idnex of what you ened to remove is 0, just return the next

        if it is

        '''
        
