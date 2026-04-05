"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied_node = Node(-102)
        iter_node = Node(-101)
        copied_node.next = iter_node

        random_retro = {}
        created_nodes = {}
        index = 0

        while head is not None:
            new_node = Node(head.val)
            
            backfills = random_retro.get(head, [])
            
            for node in backfills:
                node.random = new_node

            created_nodes[head] = new_node
            
            if head.random is None:
                new_node.random = None
            elif head.random in created_nodes:
                new_node.random = created_nodes[head.random]
            else:
                if head.random in random_retro:
                    random_retro[head.random].append(new_node)
                else:
                    random_retro[head.random] = [new_node]
        
            iter_node.next = new_node
            head = head.next
            iter_node = iter_node.next
            index += 1

        return copied_node.next.next
