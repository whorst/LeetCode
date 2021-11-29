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

def reverseLinkedList(node):
    first = node