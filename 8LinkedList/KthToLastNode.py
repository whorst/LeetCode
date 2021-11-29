class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(number, first_node):
    first_iterator = 1
    trailing_iterator = -1
    first = first_node
    trailing = None

    while first:
        if trailing_iterator == -1:
            if first_iterator - number == 0:
                trailing_iterator = 1
                trailing = first_node
        else:
            trailing = trailing.next
            trailing_iterator = trailing_iterator + 1

        first = first.next
        first_iterator += 1

    return trailing


# Returns the node with value "Devil's Food" (the 2nd to last node)


print(kth_to_last_node(2, a).value)