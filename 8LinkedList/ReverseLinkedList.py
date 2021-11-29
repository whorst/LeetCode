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
five.next = None

def reverseLinkedList(node):
    first = node

    if first.next == None:
        return first

    second = first.next

    if second.next == None:
        second.next = first
        first.next = None
        return second

    third = second.next
    first.next = None

    while True:
        second.next = first
        first = second
        second = third
        if third.next == None:
            third.next = first
            return third
        third = third.next

x = reverseLinkedList(one)
# print(x)

while (x):
    print(x.value)
    x = x.next