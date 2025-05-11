
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

#Tree Building
def build_tree():
    nodes = {}
    root = None
    
    n = int(input("Enter number of edges: "))
    print("Enter parent-child pairs:")
    
    edges = []
    for _ in range(n):
        parent, child = input().split()
        edges.append((parent, child))
        
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        
        nodes[parent].children.append(nodes[child])
        
        if root is None:
            root = nodes[parent]
    
    return root, edges

# BFS Traversal
def bfs_traversal(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        
        for child in node.children:
            queue.append(child)
            
if __name__ == "__main__":
    root, edges = build_tree()
    print("\nBFS Traversal:")
    bfs_traversal(root)
