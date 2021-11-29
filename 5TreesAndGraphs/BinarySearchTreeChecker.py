class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)


def add_to_tree(rootNode, nums):
    for num in nums:
        current = rootNode
        foundHome = False
        while (foundHome == False):
            if (num > current.value):
                if (current.right == None):
                    newNode = BinaryTreeNode(num)
                    current.right = newNode
                    foundHome = True
                else:
                    current = current.right
            if (num < current.value):
                if (current.left == None):
                    newNode = BinaryTreeNode(num)
                    current.left = newNode
                    foundHome = True
                else:
                    current = current.left


def is_valid_bst(root, lower_bound, upper_bound):
    if (root == None):
        return True

    if (float(root) > float(upper_bound) or float(root) < float(lower_bound)):
        return False

    is_left_valid = is_valid_bst(root.left, lower_bound, root)  # Visit the left
    is_rite_valid = is_valid_bst(root.right, root, upper_bound)  # Visit the right
    return is_left_valid and is_rite_valid


root = BinaryTreeNode(10)
add_to_tree(root, [5, 15, 3, 7, 13, 17, 1, 4, 6, 8, 12, 14, 16, 18])
level_list = []
root.right.right.right = BinaryTreeNode(20)
print(is_valid_bst(root, float("-inf"), float("inf")))