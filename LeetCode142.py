"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Intution: Same as 141, we use fast and slow pointers to find if there is a loop
if we find a loop, we fix the position of fast, and get another pointer(iter) starting from head
once slow completes a loop, and reaches fast again, we move the iter to next and do the check again

while this wud work might need a lot of laps till we reach the cycle entry

Better approach (not implemented here) is
Floyd's Cycle Detection Algorithm: The distance from the head to the start of the cycle is
exactly equal to the distance from the meeting point to the start of the cycle
(plus maybe a few full laps around the loop).

"""
from typing import Optional

from LeetCode141 import ListNode, create_linked_list_with_cycle


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                found = True
                break

        if not found:
            return None

        iter = head
        while slow:
            if slow == iter:
                return iter

            slow = slow.next
            if slow == fast:
                iter = iter.next

        return None
if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 0, -4]
    pos1 = 1
    head1 = create_linked_list_with_cycle(nums1, pos1)
    assert solution.detectCycle(head1).val == 2

    nums2 = [1, 2]
    pos2 = 0
    head2 = create_linked_list_with_cycle(nums2, pos2)
    assert solution.detectCycle(head2).val == 1

    nums3 = [1]
    pos3 = -1
    head3 = create_linked_list_with_cycle(nums3, pos3)
    assert solution.detectCycle(head3) == None
