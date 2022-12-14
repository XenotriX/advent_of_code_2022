from math import copysign


def get_range(start, end):
    """Custom range"""
    if start <= end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


# Parse the file
with open('input.txt', 'r') as f:
    lines = []
    blocks = set()
    while line := f.readline():
        coords = line.strip().split(' -> ')
        points = [coord.split(',') for coord in coords]
        points = [(int(x), int(y)) for x, y in points]
        lines.extend(zip(points[:-1], points[1:]))

    for line in lines:
        for y in get_range(line[0][1], line[1][1]):
            for x in get_range(line[0][0], line[1][0]):
                blocks.add((x, y))

    y_max = max([block[1] for block in blocks])
    lowest_block = []


def is_down_free(pos):
    """Checks if block below is free"""
    if pos[1] - 1 == y_max:
        return False
    new_pos = (pos[0], pos[1] + 1)
    return new_pos not in blocks


def is_left_free(pos):
    """Checks if block on the bottom left is free"""
    if pos[1] - 1 == y_max:
        return False
    new_pos = (pos[0] - 1, pos[1] + 1)
    return new_pos not in blocks


def is_right_free(pos):
    """Checks if block on the bottom right is free"""
    if pos[1] - 1 == y_max:
        return False
    new_pos = (pos[0] + 1, pos[1] + 1)
    return new_pos not in blocks


emitter = (500, 0)
count = 0
task1_count = 0
done = False

# Emmit new grains
while not done:
    pos = emitter

    # Move the grain down
    landed = False
    while not landed:
        if is_down_free(pos):
            # Move down
            pos = (pos[0], pos[1] + 1)
        elif is_left_free(pos):
            # Move left
            pos = (pos[0] - 1, pos[1] + 1)
        elif is_right_free(pos):
            # Move right
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            # Stay here
            landed = True
            blocks.add(pos)
            count += 1

        # Keep count grains fall from platforms
        if task1_count == 0 and pos[1] > y_max:
            task1_count = count
            break

    # Stop if sand is blocking the emitter
    if pos == emitter:
        done = True

print(f'(1) Grains on platforms: {task1_count}')
print(f'(2) Grains on floor: {count}')
