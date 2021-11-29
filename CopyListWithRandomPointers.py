# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head, visitedHash):

    if head == None:
        return None

    if head in visitedHash:
        return visitedHash[head]


    node = Node(head.val, None, None)

    visitedHash[head] = node

    # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
    # Thus we have two independent recursive calls.
    # Finally we update the next and random pointers for the new node created.
    node.next = copyRandomList(head.next)
    node.random = copyRandomList(head.random)

    return node