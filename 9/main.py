import math


def simulate_rope(rope, visited, direction, count):
    count = int(count)

    for i in range(count):
        if direction == 'R':
            rope[0][0] += 1
        elif direction == 'L':
            rope[0][0] -= 1
        elif direction == 'U':
            rope[0][1] += 1
        elif direction == 'D':
            rope[0][1] -= 1

        for i in range(1, len(rope)):
            x_dist = rope[i - 1][0] - rope[i][0]
            y_dist = rope[i - 1][1] - rope[i][1]
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist > math.sqrt(2):
                if abs(x_dist) > abs(y_dist):
                    rope[i][0] += int(math.copysign(1, x_dist))
                    if abs(x_dist) > 1 and abs(y_dist) > 0:
                        rope[i][1] += int(math.copysign(1, y_dist))
                else:
                    rope[i][1] += int(math.copysign(1, y_dist))
                    if abs(y_dist) > 1 and abs(x_dist) > 0:
                        rope[i][0] += int(math.copysign(1, x_dist))

        visited.add((rope[-1][0], rope[-1][1]))


with open('input.txt', 'r') as f:
    rope1 = [[0, 0], [0, 0]]
    rope2 = [[0, 0] for _ in range(10)]

    visited1 = set()
    visited2 = set()

    while line := f.readline():
        direction, count = line.strip().split(' ')
        simulate_rope(rope1, visited1, direction, int(count))
        simulate_rope(rope2, visited2, direction, int(count))

    print(f'(1) Visited by rope with length 1: {len(visited1)}')
    print(f'(2) Visited by rope with length 10: {len(visited2)}')
