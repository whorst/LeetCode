class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

one = LinkedListNode(1)
two = LinkedListNode(2)
three = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = three

def contains_cycle(node):
    id_set = set()
    while node:
        if id(node) in id_set:
            return True
        else:
            id_set.add(id(node))
        node = node.next

    return False

def contains_cycle_pointer(node):
    slow_pointer = node

    while slow_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = slow_pointer.next
        i = 0
        while i < 3:
            if fast_pointer.next == None:
                return False
            fast_pointer = fast_pointer.next
            if id(fast_pointer) == id(slow_pointer):
                return True
            i+=1

    return False


print(contains_cycle_pointer(one))
