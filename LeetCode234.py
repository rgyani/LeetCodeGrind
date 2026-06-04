"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Intution: maintain two sums, where sum1 = sum1 * 10 + i, sum2 = i * 10**(k++) + sum2
but we might face the issue where the list is large, then we can get overflows

so
1. lets find the middle of the list first by using 2 pointers, one fast and one slow
2. now reverse the second half of the list
3. simply check the two halves now

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # ompare the halves
        first_half = head
        second_half = prev
        is_pal = True

        while second_half:
            if first_half.val != second_half.val:
                is_pal = False  # Set flag instead of returning early
                break
            first_half = first_half.next
            second_half = second_half.next

        # RESTORE the list to its original state
        # Reverse the second half back (prev is currently the head of the reversed half)
        re_curr = prev
        re_prev = None
        while re_curr:
            next_node = re_curr.next
            re_curr.next = re_prev
            re_prev = re_curr
            re_curr = next_node

        return is_pal


def build_linked_list(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": [1, 2, 2, 1], "expected": True},
        {"input": [1, 2], "expected": False},
        {"input": [1], "expected": True},
        {"input": [], "expected": True},
        {"input": [1, 2, 3, 2, 1], "expected": True},
    ]

    for i, case in enumerate(test_cases):
        # Convert the array to a linked list
        head_node = build_linked_list(case["input"])
        result = solution.isPalindrome(head_node)
        # Check correctness
        assert result == case["expected"]
