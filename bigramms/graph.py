import collections as cl

my_table = {
    1: {2, 3},
    2: {1, 3, 5},
    3: {2, 4, 6},
    4: {1, 3, 6, 7},
    5: {2, 6, 8, 9},
    6: {3, 5, 7, 9},
    7: {4, 6},
    8: {5},
    9: {5, 6}
}


def bfs(v_from, v_to, table):
    path = []
    previous = {}
    visited = {i: False for i in table}
    queue = cl.deque()
    queue.append(v_from)
    previous[v_from] = -1
    visited[v_from] = True
    while len(queue) > 0:
        current_node = queue.popleft()

        if current_node not in table:
            raise KeyError(f"Не найден элемент со значением {current_node} в графе")

        if current_node == v_to:
            while current_node != -1:
                path.append(current_node)
                current_node = previous[current_node]
            break

        for node in table[current_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                previous[node] = current_node
    path.reverse()
    return path


def dfs(v_from, v_to, table):
    path = []
    previous = {}
    visited = {i: False for i in table}
    queue = cl.deque()
    queue.append(v_from)
    previous[v_from] = -1
    visited[v_from] = True
    while len(queue) > 0:
        current_node = queue.pop()

        if current_node not in table:
            raise KeyError(f"Не найден элемент со значением {current_node} в графе")

        if current_node == v_to:
            while current_node != -1:
                path.append(current_node)
                current_node = previous[current_node]
            break

        for node in table[current_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                previous[node] = current_node
    path.reverse()
    return path


for s in my_table:
    for e in my_table:
        print(f"From {s} to {e}:\n    bfs: {bfs(s, e, my_table)}\n    dfs: {dfs(s, e, my_table)}\n")
