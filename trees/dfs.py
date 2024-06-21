class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, *values):
        for value in values:
            self.children.append(TreeNode(value))
    
    def traverse(self, visited = None):
        if visited is None:
            visited = set()
        
        visited.add(self.value)
        print(self.value, end=' -> ')

        for child in self.children:
            if child.value not in visited:
                child.traverse(visited)


earth = TreeNode('Earth')
earth.add_child('Asia', 'Africa')

asia, africa = earth.children

asia.add_child('India', 'China', 'South Korea')

africa.add_child('Nigeria')
africa.add_child('Senegal')
africa.add_child('Angola')

print('Traversing Earth (DFS)')
earth.traverse()
print('END')