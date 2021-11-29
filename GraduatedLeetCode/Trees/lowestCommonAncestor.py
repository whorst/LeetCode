def lowestCommonAncestor(self, root, p, q):
    if not root or not p or not q:
        return None
    if (max(p.val, q.val) < root.val):
        return lowestCommonAncestor(root.left, p, q)
    elif (min(p.val, q.val) > root.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
