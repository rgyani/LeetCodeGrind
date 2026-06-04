# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_array(head:Optional[ListNode]):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result

def build_linked_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def build_linked_list_with_cycle(arr: list[int], pos: int) -> Optional[ListNode]:
    if not arr:
        return None

    # Create the head node
    head = ListNode(arr[0])
    current = head

    # Keep track of nodes to easily hook up the cycle later
    node_list = [head]

    # Build the rest of the list
    for val in arr[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        node_list.append(new_node)

    # If pos is valid, connect the last node to the node at index 'pos'
    if pos != -1 and pos < len(node_list):
        current.next = node_list[pos]

    return head