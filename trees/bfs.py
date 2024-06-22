from collections import deque

LETTERS = {
  'A' : ['B', 'C', 'D'],
  'B' : ['A', 'E'],
  'C' : ['A', 'F','G'],
  'D' : ['A', 'H'],
  'E' : ['B', 'I'],
  'F' : ['C'],
  'G' : ['C', 'J'],
  'H' : ['D'],
  'I' : ['E'],
  'J' : ['G']
}

def bfs(tree, root):
    path = []
    visited = set()
    queue = deque([])

    queue.append(root)

    while queue:
        node = queue.popleft()
        visited.add(node)
        path.append(node)

        for child in tree[node]:
            if child not in visited:
                queue.append(child)
    
    return path


print('BFS Traverse')
paths = bfs(tree=LETTERS, root='A')
print(' -> '.join(paths))
print('END')