class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)

    def value(self):
        return self.val

class DoublyLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, node):
        if (self.head == None and self.tail == None):
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def removeTail(self):
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return node

    def remove(self, node):
        if self.head is self.tail:
            self.head == None
            self.tail == None
            return node
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
            node.next = None
            return node
        elif node is self.tail:
            return self.removeTail()

        prev = node.prev
        next = node.next
        node.next = None
        node.prev = None
        prev.next = next
        next.prev = prev
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.keyDict = {}
        self.doublyLinked = DoublyLinked()

    def get(self, key: int) -> int:
        if key in self.keyDict:
            self.doublyLinked.remove(self.keyDict[key])
            self.doublyLinked.addHead(self.keyDict[key])
            return self.keyDict.get(key)
        else:
            return -1


    def put(self, key, value) -> None:
        if key in self.keyDict:
            old = self.keyDict[key]
            new = Node(key, value)
            self.keyDict[key] = new

            self.doublyLinked.remove(old)
            self.doublyLinked.addHead(new)
        elif self.currSize == 0:
            new = Node(key, value)
            self.keyDict[key] = new
            self.doublyLinked.addHead(new)
            self.currSize += 1
        elif self.currSize > 0 and self.currSize < self.capacity:
            new = Node(key, value)
            self.keyDict[key] = new
            self.doublyLinked.addHead(new)
            self.currSize += 1
        elif self.currSize == self.capacity:
            new = Node(key, value)
            self.keyDict[key] = new
            self.doublyLinked.addHead(new)
            x = self.doublyLinked.removeTail()
            self.keyDict.pop(x.key)