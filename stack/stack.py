class Stack:
    def __init__(self, max_size = 3):
        self.max_size = max_size
        self.items = []
    
    def push(self, value):
        if len(self.items) < self.max_size:
            self.items.append(value)
        else:
            raise Exception('StackOverflow - Max Size reached!')

    def pop(self):
        if self.is_empty():
            return None
        
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

print(f"Is empty? {stack.is_empty()}")
print(f"Peek: {stack.peek()}")

stack.push('todo 1')

print(f"Is empty? {stack.is_empty()}")
print(f"Peek: {stack.peek()}")

stack.push('todo 2')
stack.push('todo 3')

print(f"Stack items: {stack.items}")
print(f"Peek: {stack.peek()}")

print(f"Pop: {stack.pop()}")

print(f"Stack items: {stack.items}")
print(f"Peek: {stack.peek()}")

for _ in range(len(stack.items)):
    print(f"Pop: {stack.pop()}")

print(f"Stack items: {stack.items}")
print(f"Peek: {stack.peek()}")

print(f"Pop: {stack.pop()}")
