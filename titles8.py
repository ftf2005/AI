import copy
from heapq import heappush, heappop

n = 3
rows, cols = [1, 0, -1, 0], [0, -1, 0, 1]

class Node:
    def __init__(self, parent, mats, empty_tile_posi, costs, levels):
        self.parent = parent
        self.mats = mats
        self.empty_tile_posi = empty_tile_posi
        self.costs = costs
        self.levels = levels

    def __lt__(self, nxt):
        return self.costs < nxt.costs

def calculate_costs(mats, final):
    return sum(mats[i][j] and mats[i][j] != final[i][j] for i in range(n) for j in range(n))

def move_tile(mats, empty_tile_posi, new_empty_tile_posi):
    new_mats = copy.deepcopy(mats)
    x1, y1 = empty_tile_posi
    x2, y2 = new_empty_tile_posi
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]
    return new_mats

def print_matrix(mats):
    for row in mats:
        print(" ".join(map(str, row)))
    print()

def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n

def print_path(root):
    if root:
        print_path(root.parent)
        print_matrix(root.mats)

def solve(initial, empty_tile_posi, final):
    pq = []
    costs = calculate_costs(initial, final)
    root = Node(None, initial, empty_tile_posi, costs, 0)
    heappush(pq, root)

    while pq:
        minimum = heappop(pq)
        if minimum.costs == 0:
            print_path(minimum)
            return

        for dx, dy in zip(rows, cols):
            new_pos = [minimum.empty_tile_posi[0] + dx, minimum.empty_tile_posi[1] + dy]
            if is_safe(*new_pos):
                new_mats = move_tile(minimum.mats, minimum.empty_tile_posi, new_pos)
                new_node = Node(minimum, new_mats, new_pos, calculate_costs(new_mats, final), minimum.levels + 1)
                heappush(pq, new_node)

# Main Code
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_posi = [1, 2]

solve(initial, empty_tile_posi, final)
