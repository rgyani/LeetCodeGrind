"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Intution: Slow and fast pointers, keep walking thru the list till they meet
U loop till fast.next is available, cause if the linkedlist does not have a loop, it will exit here
"""
from typing import Optional

from LinkedList import ListNode, build_linked_list_with_cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False




if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 0, -4]
    pos1 = 1
    head1 = build_linked_list_with_cycle(nums1, pos1)
    assert solution.hasCycle(head1) == True

    nums2 = [1, 2]
    pos2 = 0
    head2 = build_linked_list_with_cycle(nums2, pos2)
    assert solution.hasCycle(head2) == True

    nums3 = [1]
    pos3 = -1
    head3 = build_linked_list_with_cycle(nums3, pos3)
    assert solution.hasCycle(head3) == False
