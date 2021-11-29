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


root = BinaryTreeNode(10)
add_to_tree(root, [5, 15, 3, 7, 13, 17, 1, 4,6,8, 12, 14, 16, 18])
level_list = []


def is_super_balanced(node_list, level, level_list):
    new_list = []
    for node in node_list:
        if node.left == None and node.right == None:
            if (len(level_list) == 0 or level_list[len(level_list) - 1] != level):
                level_list.append(level)
                if(level - level_list[0] > 1):
                    return False
        else:
            if (node.left != None):
                new_list.append(node.left)
            if (node.right != None):
                new_list.append(node.right)

    if (len(node_list) > 0):
        level = level + 1
        return is_super_balanced(new_list, level, level_list)
    return True

leaf_dict = {}
node_list = [root]
print(is_super_balanced(node_list, 0, level_list))
# lowest = None
# for level in level_list:
#     print(level)
