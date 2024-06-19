class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, value):
        previous_node = None
        current_node = self.head

        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        while current_node:
            if current_node.value == value:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node == None:
            return
        
        if self.tail == current_node:
            self.tail = previous_node

        previous_node.next = current_node.next
        current_node = None

    def print(self, reverse=False):
        if reverse:
            self.print_reverse()
            return
        
        node = self.head 
        while node:
            print(node.value, end=" => " if node.next else "\n")
            node = node.next 
    
    def print_reverse(self):
        stack = []
        current_node = self.head

        while current_node:
            stack.append(current_node.value)
            current_node = current_node.next
        
        while stack:
            node = stack.pop()
            print(node, end=" => " if stack else "\n")


my_list = LinkedList()
my_list.insert('Task A')
my_list.insert('Task B')
my_list.insert('Task C')

my_list.print()
my_list.delete('Task C')
my_list.print()

print("Reverse traversal")
my_list.print(reverse=True)
my_list.print_reverse()