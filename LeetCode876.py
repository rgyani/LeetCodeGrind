"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

keep it simple stupid, count elements, keep moving i from 0 to count/2

OR
1 2 3 4 5
if i=0, j=0, i+=1, j+=2 when j = n we reach i as the center
1,3 -> 2, 5, 3, none

1 2 3 4 5 6
1, 3 -> 2, 5 -> 3, None
"""
from typing import Optional

from LinkedList import ListNode, build_linked_list, to_array


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        i = head
        j = head

        odd = True
        while j and j.next:
            i = i.next
            j = j.next
            if j:
                j = j.next
            else:
                odd = False

        if odd:
            return i
        else:
            return i.next



if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3,4,5]
    head1 = build_linked_list(nums1)
    assert to_array(solution.middleNode(head1)) == [3,4,5]

    nums1 = [1,2,3,4,5,6]
    head1 = build_linked_list(nums1)
    assert to_array(solution.middleNode(head1)) == [4,5, 6]

    nums1 = []
    head1 = build_linked_list(nums1)
    assert to_array(solution.middleNode(head1)) == []

    nums1 = [1]
    head1 = build_linked_list(nums1)
    assert to_array(solution.middleNode(head1)) == [1]

    nums1 = [1, 2]
    head1 = build_linked_list(nums1)
    assert to_array(solution.middleNode(head1)) == [2]
