from collections import deque


class Queue:
    def __init__(self):
        self.items = deque([])

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.popleft()
        else:
            return None
            
    def __str__(self) -> str:
        return ', '.join(self.items)


queue = Queue()
queue.enqueue('Task A')
queue.enqueue('Task B')
queue.enqueue('Task C')

print(queue)

while queue.items:
    print(f"Removing task: {queue.dequeue()}")

print(f"Removing task: {queue.dequeue()}")