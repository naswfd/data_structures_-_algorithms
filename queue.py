class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isSize(self):
        return len(self.items)


q = Queue()
print(q.isSize())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
