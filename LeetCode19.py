"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Intution
1 2 3 4 5  n = 2
if i = 0, j = 2 and we keep incrementing both i and, we reach
2 4-> 3 5

so 2 pointers, j gets a head start of n, then we move i and j, when j reaches end, i is n steps behind j

1 2  and n = 2
the above will fail for this condition
unless we introduce a dummy node before head

so [dummy 1 2]
     i         j

"""
from typing import Optional

from LinkedList import ListNode, build_linked_list, to_array


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return None

        dummy = ListNode(0, head)

        i = dummy
        j = head

        while n:
            if j:
                j = j.next
            n -=1

        while j:
            i = i.next
            j = j.next

        i.next = i.next.next
        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3,4,5]
    head1 = build_linked_list(nums1)
    assert to_array(solution.removeNthFromEnd(head1, 2)) == [1,2,3,5]

    nums3 = [1]
    head3 = build_linked_list(nums3)
    assert to_array(solution.removeNthFromEnd(head3, 1)) == []

    nums2 = [1, 2]
    head2 = build_linked_list(nums2)
    assert to_array(solution.removeNthFromEnd(head2, 1)) == [1]

    nums2 = [1, 2]
    head2 = build_linked_list(nums2)
    assert to_array(solution.removeNthFromEnd(head2, 2)) == [2]

