from collections import deque

grid = [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

start, goal = (0, 0), (5, 5)


def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0

    while queue:
        curr, path = queue.popleft()
        expanded += 1

        if curr == goal:
            return path, len(path) - 1, expanded

        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < 6
                and 0 <= nc < 6
                and grid[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
