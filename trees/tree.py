class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, nodes):
        for node in nodes:
            self.children.append(node)

    def remove_child(self, node):
        self.children = [child for child in self.children if child is not node]


def traverse_tree(node):
    print(node.value, end=' -> ')
    for child in node.children:
        traverse_tree(child)


root_node = Node('Engineering')

web_node = Node('Web')
data_node = Node('Data')
design_node = Node('Design')

design_node.add_children([Node('UX'), Node('UI')])
web_node.add_children([Node('Full-Stack'), Node('Front-end'), Node('Back-end')])
data_node.add_children([Node('Data-Analyst'), Node('Data-Scientist'), Node('Data-Engineer')])

root_node.add_child(web_node)
root_node.add_child(data_node)
root_node.add_child(design_node)

traverse_tree(root_node)