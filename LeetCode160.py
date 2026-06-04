"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.



Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Intution: if i walks to the end of list A, and j walks to the end of listB, and they switch the heads, the next time they walk they will move in the middle
"""
from typing import Optional

from LinkedList import ListNode, build_linked_list, to_array


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        i = headA
        j = headB

        # If they intersect, they will meet at the intersection node.
        # If they don't, they will both hit None at the same time and exit.
        while i != j:
            i = i.next if i else headB
            j = j.next if j else headA

        return i

def create_intersecting_lists(listA_vals:list, listB_vals:list, intersect_vals):
    intersect_head = None
    intersect_tail = None
    for val in intersect_vals:
        node = ListNode(val)
        if not intersect_head:
            intersect_head = node
            intersect_tail = node
        else:
            intersect_tail.next = node
            intersect_tail = node

    dummyA = ListNode(0)
    curr = dummyA
    for val in listA_vals:
        curr.next = ListNode(val)
        curr = curr.next
    curr.next = intersect_head

    dummyB = ListNode(0)
    curr = dummyB
    for val in listB_vals:
        curr.next = ListNode(val)
        curr = curr.next
    curr.next = intersect_head

    return dummyA.next, dummyB.next, intersect_head

if __name__ == "__main__":
    solution = Solution()

    headA, headB, expected = create_intersecting_lists([4, 1], [5, 6, 1], [8, 4, 5])
    result = solution.getIntersectionNode(headA, headB)
    assert result == expected

    headA, headB, expected = create_intersecting_lists([2, 6, 4], [1, 5], [])
    result = solution.getIntersectionNode(headA, headB)
    assert result is None

    headA, headB, expected = create_intersecting_lists([], [], [1, 2, 3])
    result = solution.getIntersectionNode(headA, headB)
    assert result == expected
