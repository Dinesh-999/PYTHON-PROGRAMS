# queue program
# queue means first in first out

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()
print(queue.is_empty())

for i in range(0, 10):
    queue.enqueue(i)  # inserts the elements in queue

print(queue.size())  # returns the size of the queue
print(queue.items)  # returns the items in the queue
print(queue.dequeue())  # deletes the last element  (means deletes the first element inserted)
# above statement deletes only one elements (0)

for i in range(queue.size()):
    print(queue.dequeue())
