# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

    def mergeList(self, l1, l2):
        # print(l1.val)
        # print(l2.val)
        start_node = ListNode()
        iter_node = ListNode()
        start_node.next = iter_node
        next_node = 'l1'
        while l1 is not None and l2 is not None:
            if next_node == 'l1':
                iter_node.next = l1
                next_node = 'l2'
                iter_node = iter_node.next
                l1 = l1.next
            else:
                iter_node.next = l2
                next_node = 'l1'
                iter_node = iter_node.next
                l2 = l2.next
        if l1 is not None:
            iter_node.next = l1
        elif l2 is not None:
            iter_node.next = l2
        
        return start_node.next.next


    def reorderList(self, head: Optional[ListNode]) -> None:
        num_nodes = 0
        counter_node = head
        while counter_node is not None:
            num_nodes += 1
            counter_node = counter_node.next
        halfway_point = num_nodes // 2
        print(num_nodes, halfway_point)
        iter_node = head
        while halfway_point > 0:
            iter_node = iter_node.next
            halfway_point -= 1
        
        second_half = iter_node.next
        # print(iter_node.val, second_half.val)
        iter_node.next = None

        reversed_second_half = self.reverseList(second_half)

        self.mergeList(head, reversed_second_half)



