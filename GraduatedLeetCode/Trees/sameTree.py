# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        p_queue = []
        q_queue = []

        p_queue.append(p)
        q_queue.append(q)

        if (q == None and p == None):
            return True

        if (q == None and p or p == None and q):
            return False

        while (len(p_queue) != 0 and len(q_queue) != 0):
            if (len(p_queue) != len(q_queue)):
                return False

            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)

            if (p_curr.val == q_curr.val):
                if (p_curr.left):
                    if (q_curr.left == None):
                        return False
                    p_queue.append(p_curr.left)
                if (p_curr.right):
                    if (q_curr.right == None):
                        return False
                    p_queue.append(p_curr.right)

                if (q_curr.left):
                    if (p_curr.left == None):
                        return False
                    q_queue.append(q_curr.left)
                if (q_curr.right):
                    if (p_curr.right == None):
                        return False
                    q_queue.append(q_curr.right)
            else:
                return False
        return True
