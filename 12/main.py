class Node:
    def __init__(self, value, pos) -> None:
        self.value = value
        self.pos = pos
        self.neigbours = []
        self.path_length = None

    def add_edge(self, node):
        self.neigbours.append(node)

    def __str__(self) -> str:
        return (
            f'Node {self.pos}\n'
            f'- Value: {self.value}\n'
            f'- Path length: {self.path_length}'
        )

def find_neigbours(map, node):
    neigbours = []
    val = map[node.pos[0]][node.pos[1]].value
    if node.pos[0] > 0 and map[node.pos[0] - 1][node.pos[1]].value - val <= 1:
        neigbours.append(map[node.pos[0] - 1][node.pos[1]])
    if node.pos[0] < len(map) - 1 and map[node.pos[0] + 1][node.pos[1]].value - val <= 1:
        neigbours.append(map[node.pos[0] + 1][node.pos[1]])
    if node.pos[1] > 0 and map[node.pos[0]][node.pos[1] - 1].value - val <= 1:
        neigbours.append(map[node.pos[0]][node.pos[1] - 1])
    if node.pos[1] < len(map[0]) - 1 and map[node.pos[0]][node.pos[1] + 1].value - val <= 1:
        neigbours.append(map[node.pos[0]][node.pos[1] + 1])
    return neigbours


def explore(map, node):
    neigbours = find_neigbours(map, node)
    for neigbour in neigbours:
        node.add_edge(neigbour)

def estimate_path_length(node, end):
    dist = abs(end[0] - node.pos[0]) + abs(end[1] - node.pos[1])
    return node.path_length + dist

def search():
    while len(frontier) != 0:
        frontier.sort(key=lambda x: estimate_path_length(x, end))
        node = frontier.pop(0)

        for neigbour in node.neigbours:
            if neigbour not in visited:
                frontier.append(neigbour)
                visited.add(neigbour)
            if neigbour.path_length is None or node.path_length + 1 < neigbour.path_length:
                neigbour.path_length = node.path_length + 1
            if neigbour is end_node:
                return neigbour

    raise Exception('Could not find the end node')

# Parse the input file
with open('input.txt', 'r') as f:
    map = []
    row_index = 0
    start = None
    end = None

    while line := f.readline():
        line = list(line.strip())
        if 'S' in line:
            col = line.index('S')
            line[col] = 'a'
            start = (row_index, col)
        if 'E' in line:
            col = line.index('E')
            line[col] = 'z'
            end = (row_index, col)

        row = [Node(ord(el) - ord('a'), (row_index, index)) for index, el in enumerate(line)]
        map.append(row)
        row_index += 1

if not start or not end:
    raise Exception('Missing start or end')

# Find all the edges
for row in map:
    for node in row:
        explore(map, node)

# Task 1: Start from the 'S'
start_node = map[start[0]][start[1]]
start_node.path_length = 0
end_node = map[end[0]][end[1]]

frontier = [start_node]
visited = set([start_node])

task1 = search().path_length

# Task 2: Add all 'a' nodes to the frontier and reset the path_length
frontier = []
visited = set()
for row in map:
    for node in row:
        node.path_length = None
        if node.value == 0:
            frontier.append(node)
            visited.add(node)
            node.path_length = 0

task2 = search().path_length

print(f'(1) Path length from start: {task1}')
print(f'(2) Path length from any \'a\': {task2}')

