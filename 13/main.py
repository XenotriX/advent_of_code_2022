from itertools import zip_longest
from functools import cmp_to_key

# Compares two packets
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    # It's a list -> Compare element-wise
    for l, r in zip_longest(left, right):
        # One of the lists might be shorter
        if l is None:
            return -1
        elif r is None:
            return 1

        # Compare the element
        cmp = compare(l, r)
        if cmp == 0:
            continue
        else:
            return cmp
    return 0

# Read the packets and count number of ordered pairs
packets = []
with open('input.txt', 'r') as f:
    count = 0 # Number of correct pairs
    index = 1 # Current pair index
    while line1 := f.readline():
        line2 = f.readline()
        f.readline() # Blank line

        # Parse using eval (I know)
        left = eval(line1.strip())
        right = eval(line2.strip())

        # Store packets for task 2
        packets.append(left)
        packets.append(right)

        # Count if left < right
        count += index if compare(left, right) == -1 else 0
        index += 1

# Sort the packets including dividers
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare))

# Caculate decoder key
decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f'(1) Sum of correct indicies: {count}')
print(f'(2) Decoder key: {decoder_key}')
