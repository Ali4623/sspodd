graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
    }
def dfs(node,visited=None):
    if visited is None:
        visited=set()
    if node not in visited:
            print(node,end='')
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour,visited)
def bfs(start_node):
    visited=set()
    queue=[start_node]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node,end='')
            visited.add(node)
            queue.extend(graph[node])
print("DFS traversal:")
dfs("A")
print("\nBFS Traversal:")
bfs("A")
