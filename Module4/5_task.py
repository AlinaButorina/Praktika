def find_all_paths(graph, start, end):
    def dfs(current, path):
        path.append(current)
        if current == end:
            paths.append(path[:])
        else:
            for neighbor in graph.get(current, []):
                dfs(neighbor, path)

        path.pop()

    paths = []
    dfs(start, [])
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
paths = find_all_paths(graph, start, end)
for path in paths:
    print(path)
