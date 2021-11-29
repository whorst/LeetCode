# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if (head.next == None):
            return head

        curr_node = head
        curr_number = 0
        position_dict = {}

        while curr_node:
            position_dict[curr_number] = curr_node
            curr_node = curr_node.next
            curr_number += 1

        curr_number -= 1
        curr = None
        head = curr
        min_pointer = 0
        max_pointer = curr_number

        while min_pointer < max_pointer:
            if (curr == None):
                curr = position_dict.get(min_pointer)
            else:
                curr.next = position_dict.get(min_pointer)
                curr = curr.next
            curr.next = position_dict.get(max_pointer)
            curr = curr.next
            min_pointer += 1
            max_pointer -= 1

        if min_pointer == max_pointer:
            curr.next = position_dict.get(min_pointer)
            curr = curr.next
            curr.next = None

        curr.next = None

        print(head)