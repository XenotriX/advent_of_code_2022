import re
from tqdm import tqdm

sensors = []
beacons = set()
y_focus = 2000000


def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open('input.txt', 'r') as f:
    while line := f.readline():
        matches = re.match(
            ".*x=(-?\\d+), y=(-?\\d+):.*x=(-?\\d+), y=(-?\\d+)", line.strip())
        sensor = (int(matches.group(1)), int(matches.group(2)))
        beacon = (int(matches.group(3)), int(matches.group(4)))
        rng = dist(sensor, beacon)
        sensors.append((sensor, rng))
        beacons.add(beacon)

blocks = set()
for pos, rng in sensors:
    y_dist = rng - abs(pos[1] - y_focus)
    for x in range(pos[0] - y_dist, pos[0] + y_dist + 1):
        blocks.add((x, y_focus))

print(f'(1) Number of coverd areas on line {y_focus}: {len(blocks - beacons)}')

beacon_pos = None
for y in tqdm(range(0, 4000001)):
    intervals = list()
    for pos, rng in sensors:
        y_dist = rng - abs(pos[1] - y)
        if y_dist <= 0:
            continue
        intervals.append(([pos[0] - y_dist, pos[0] + y_dist + 1]))

    merged_intervals = merge(intervals)
    if len(merged_intervals) > 1:
        x = merged_intervals[0][1]
        beacon_pos = (x, y)
        break

x, y = beacon_pos
print(f'(2) Found beacon: {x}, {y} = {x * 4000000 + y}')
