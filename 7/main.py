class Node:
    def __init__(self, name, parent, size) -> None:
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size

    def add_child(self, name, size):
        self.children.append(Node(name, self, size))

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise Exception(f'No child named {name} in node {self.name}')

    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)

    def is_dir(self):
        return len(self.children) > 0


# Build the tree
root = Node('/', None, 0)
with open('input.txt', 'r') as f:
    current_dir = root
    while line := f.readline():
        # Parse cd
        if line.startswith('$ cd'):
            path = line.strip().split(' ')[-1]
            if path == '/':
                current_dir = root
            elif path == '..':
                assert current_dir.parent is not None
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(path)
        elif line.startswith('$ ls'):
            pass
        else:
            size, name = line.strip().split(' ')
            if size == 'dir':
                current_dir.add_child(name, 0)
            else:
                current_dir.add_child(name, int(size))
                current_dir.add_size(int(size))


# Sums up the size of all directories smaller than 10k
def count_size(node):
    sum = 0
    for child in node.children:
        if child.is_dir():
            if child.size <= 100000:
                sum += child.size
            sum += count_size(child)
    return sum


print(f'(1) Total of dirs smaller 100k: {count_size(root)}')


# Finds all the directories larger than min_size
def find_min_size(node, min_size):
    dirs = []
    for child in node.children:
        if child.is_dir():
            if child.size >= min_size:
                dirs.append(child)
            dirs.extend(find_min_size(child, min_size))
    return dirs


# Find the smallest directory that frees enough space
min_size = 30000000 - (70000000 - root.size)
dirs = sorted(find_min_size(root, min_size), key=lambda dir: dir.size)

print(f'(2) Size of smallest dir larger than {min_size}: {dirs[0].size}')
