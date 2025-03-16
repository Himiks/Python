import queue
n = int(input())
m = int(input())

maze = []

def find_shortest(maze):
    gold = 0
    find_way = False
    start_pos = (0, 0)
    end = (m - 1, n - 1)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        if (row, col) == end:
            return path


        neighbors = find_neighbors(maze, row, col)

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
    return "IMPOSSIBLE"


def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors




for i in range(m):
    row = []
    for j in range(n):
        cell = input(f"Введите элемент ({i}, {j}): ")
        row.append(cell)

    maze.append(row)
shortest_path = find_shortest(maze)

gold_count = False
gold = 0
for step in shortest_path:
    if step == (0, 0):
        continue
    if gold_count == False:
        gold += 2
        gold_count = True
    else:
        gold += 1
        gold_count = False


print(gold)





