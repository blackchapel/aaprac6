#FORD FULKERSON

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True
    while queue:
        current = queue.pop(0)
        for ind, val in enumerate(graph[current]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = current
    return True if visited[t] else False
 
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        t = sink
        while t != source:
            path_flow = min(path_flow, graph[parent[t]][t])
            t = parent[t]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
print("Maximum flow:", ford_fulkerson(graph, source, sink))