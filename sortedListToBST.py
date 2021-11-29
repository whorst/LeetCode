class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next

        def build_bst(left, right):

            if (left > right):
                return
            middle = left + (right - left) // 2

            return TreeNode(array[middle], build_bst(left, middle - 1), build_bst(middle + 1, right))

        return build_bst(0, len(array) - 1)