'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''
from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(1) Memory 
def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head.next

    while slow is not None and fast is not None:
        if slow == fast:
            return True
        slow = slow.next

        # there is no cycle, traversal came to an end
        if fast.next is None:
            return False

        fast = fast.next.next

    return False
    


A = ListNode(0)
B = ListNode(-1)
C = ListNode(-1)

A.next = B 
B.next = C 
C.next = B

print(hasCycle(A)) # true

A = ListNode(0)
B = ListNode(-1)
C = ListNode(-1)

A.next = B 
B.next = C 
C.next = None

print(hasCycle(A)) # False