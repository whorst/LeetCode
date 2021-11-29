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


def isSuperBalanced(node_list, level_list, depth):
    new_nodes = []

    while len(node_list) > 0:
        node = node_list.pop()
        if node.left != None:
            new_nodes.append(node.left)
        if node.right != None:
            new_nodes.append(node.right)
        if node.left == None and node.right == None:
            level_list.append(depth)
            if depth - level_list[0] > 1:
                return False

    if len(new_nodes) == 0:
        return True
    else:
        return isSuperBalanced(new_nodes, level_list, depth + 1)


root = BinaryTreeNode(10)
add_to_tree(root, [5, 15, 3, 7, 13, 17, 1, 4, 6, 8, 12, 14, 16, 18])
level_set = []

print(isSuperBalanced([root], level_set, 1))
