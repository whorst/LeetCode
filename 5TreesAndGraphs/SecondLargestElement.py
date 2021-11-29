# Find 2nd largest element in BST

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

    def __int__(self):
        return self.value

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


def find_second_largest_element(current, ancestor, largest):
    if (ancestor == None):
        ancestor = current
    if (current.right != None):
        while (current.right != None):
            ancestor = current
            current = current.right
        if (largest == None):
            if ancestor.left == None:
                return ancestor, current
            else:
                second_largest = find_second_largest_element(ancestor.left, ancestor, current)
                return second_largest, current
        else:
            return current


def bad_find_second_largest_element(current, ancestor, largest):
    if ancestor == None:
        if current.right != None:
            if (int(current.right) > int(largest)):
                return bad_find_second_largest_element(current.right, current, current.right)
        else:
            x = bad_find_second_largest_element(root.left, root, root)
            return x, root

    elif (current.right != None):
        if (int(current.right) > int(largest)):
            return bad_find_second_largest_element(current.right, current, current.right)
        return bad_find_second_largest_element(current.right, current, largest)

    elif (current.right == None):
        if (current == largest):
            if (current.left != None):
                left_largest = bad_find_second_largest_element(current.left, current, largest)
                return left_largest, largest
            elif (ancestor.left == None):
                return ancestor, current
            else:
                curr = ancestor.left
                while True:
                    if (curr.right == None):
                        return curr, largest
                    else:
                        curr = curr.right
        else:
            return current


root = BinaryTreeNode(10)
add_to_tree(root, [5, 3, 7, 13, 17, 15, 1, 4, 6, 8, 12, 14, 16])
# add_to_tree(root, [5, 3, 1, 4, 6,7,8,9])
level_list = []

second, largest = find_second_largest_element(root, None, root)

print(second, largest)
