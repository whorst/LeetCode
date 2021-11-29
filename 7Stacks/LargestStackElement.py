class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.max = None

    def push(self, item):
        """Push a new item onto the stack"""
        if self.max == None:
            self.max = item
        else:
            if item > self.max:
                self.max = item
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        else:
            ret_val = self.items.pop()
            if len(self.items) == 0:
                self.max = None
            elif self.max == ret_val:
                temp = None
                for item in self.items:
                    if temp == None:
                        temp = item
                    else:
                        if item > temp:
                            temp = item
                self.max = temp
        return ret_val

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def getMax(self):
        return self.max