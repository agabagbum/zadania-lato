def longes_path(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for x, y in edges:
        graph[x].append(y)
    in_degree[y] += 1
    topo_order = []
    queue = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.pop(0) 
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    dp = [0] * (N + 1)
    for u in topo_order:
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + 1)
    return max(dp)
data = input().split()
N = int(data[0])
M = int(data[1])
edges = [(int(data[2 + 2 * i]), int(data[2 + 2 * i + 1])) for i in range(M)]
print(longes_path(N, M, edges))

    
    

