"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Intution:
Start with
prev = none
current = head
    temp = current.next
    current.next = prev
    prev = current
    current = temp


"""
from LinkedList import ListNode, build_linked_list, to_array


def reverse(head:ListNode)->ListNode:
    prev= None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev

if __name__ == "__main":
    assert to_array(reverse(build_linked_list([1,2,3,4,5]))) == [5,4,3,2,1]
    assert to_array(reverse(build_linked_list([1,2]))) == [2,1]
    assert to_array(reverse(build_linked_list([1]))) == [1]