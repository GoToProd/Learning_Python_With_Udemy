graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# v_list = []
# queue = []
# def bfs(v_list, graph, node):
#     v_list.append(node)
#     queue.append(node)
    
#     while queue:
#         s = queue.pop()
#         print(s, end='')
        
#     for i in graph[s]:
#         if i not in v_list:
#             v_list.append(i)
#             queue.append(i)
            
# bfs(v_list, graph, 'D')

# graph = {
#     0: [1, 2],
#     1: [4, 3],
#     2: [3],
#     3: [5],
#     4: [6],
#     5: []
# }

def dfs(graph, node, v_list=None):
    if v_list is None:
        v_list = set()
    v_list.add(node)
    print(node)

    if node in graph:
        for i in set(graph[node]) - v_list:
            dfs(graph, i, v_list)
    return v_list

print(dfs(graph, 'C'))
