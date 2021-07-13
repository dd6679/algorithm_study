from collections import defaultdict, deque

def solution(n, path, order):
    graph = defaultdict(list)
    visited = [0 for _ in range(n) ]
    visited[0] = 1

    for p in path:
        v, w = p
        graph[v].append(w)
        graph[w].append(v)
    
    order1, order2 = {}, {}
    for u, v in order :
        order1[u] = v
        order2[v] = u
        if v == 0:
            return False
        if u == 0:
            order1[0] = 0

    queue = deque()
    queue.append(0)

    while queue :
        cur = queue.popleft()
        if cur == order1.get(order2.get(cur)) :
            visited[cur] = 2
        else :
            for node in graph[cur] :
                if visited[node] == 0 :
                    queue.append(node)
                    visited[node] = 1
                    if order1.get(node) :
                        if visited[order1[node]] == 2 :
                            queue.append(order1[node])
                            visited[order1[node]] == 1
                        order1[node] = 0
    for i in visited :
        if not i :
            return False
    return True
