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
        node = self.head

        if not node == None and node.value == value:
            self.head = node.next
            node = None
            return

        while not node == None:
            if node.value == value:
                break
            previous_node = node
            node = node.next

        if node == None:
            return
        
        previous_node.next = node.next
        node = None

    def print(self):
        node = self.head 
        while not node == None:
            print(node.value, end=" => ")
            node = node.next 


my_list = LinkedList()
my_list.insert('Task A')
my_list.insert('Task B')
my_list.insert('Task C')

my_list.print()
my_list.delete('Task B')

print()
my_list.print()
