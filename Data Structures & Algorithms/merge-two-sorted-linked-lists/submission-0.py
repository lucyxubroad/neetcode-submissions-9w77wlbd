# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_node = ListNode()
        iter_node = ListNode()
        start_node.next = iter_node

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                next_node = list1.next
                list1.next = None
                iter_node.next = list1
                list1 = next_node
                iter_node = iter_node.next
            else:
                next_node = list2.next
                list2.next = None
                iter_node.next = list2
                list2 = next_node
                iter_node = iter_node.next

        if list1 is not None:
            iter_node.next = list1
        elif list2 is not None:
            iter_node.next = list2

        return start_node.next.next