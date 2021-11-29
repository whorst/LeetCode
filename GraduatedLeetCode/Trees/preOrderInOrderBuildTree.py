class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def call(preorder, inorder):
    def array_to_tree(left, right, preorder_arr):
        # if there are no elements to construct the tree
        if left > right:
            return None

        # select the preorder_index element as the root and increment it
        root_value = preorder[preorder_arr[0]]
        root = TreeNode(root_value)
        preorder_arr[0] += 1

        # build left and right subtree
        # excluding inorder_index_map[root_value] element because it's the root
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1, preorder_arr)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right, preorder_arr)

        return root

    preorder_index = 0

    # build a hashmap to store value -> its index relations
    inorder_index_map = {}
    for index, value in enumerate(inorder):
        inorder_index_map[value] = index

    x = array_to_tree(0, len(preorder) - 1, [preorder_index])
    return x

print(call([3,9,20,15,7], [9,3,15,20,7]))