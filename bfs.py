graph = {}

queue = []
reached = []


def bfs(queue, reached, start_vertex, end_vertex):
    queue.append(start_vertex)
    reached.append(start_vertex)

    d = 0

    while queue:
        d += 1
        x = queue.pop(0)

        for i in graph[y]:
            if i not in reached:
                queue.append(i)
                reached.append(i)
            if i == end_vertex:
                return d
