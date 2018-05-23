class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)


s = Stack()
print(s.is_empty())
s.push(1)
s.push('two')
print(s.peek())
print(s.size())
