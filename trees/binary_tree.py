class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_traverse(node):
    if node is None:
        return
    in_order_traverse(node.left)
    print(node.value, end=' -> ')
    in_order_traverse(node.right)


root = Node('A')

top_left = Node('B')
top_left.left = Node('B-L')
top_left.right = Node('B-R')

top_right = Node('C')
top_right.left = Node('C-L')
top_right.right = Node('C-R')

root.left = top_left
root.right= top_right

in_order_traverse(root)