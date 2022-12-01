buffer = []
elves = []

with open('input.txt', 'r') as f:
    while line := f.readline():
        if line == '\n':
            s = sum(buffer)
            print(f'New elf: {s}')
            elves.append(s)
            buffer = []
        else:
            buffer.append(int(line))

print(f'Top elf: {sorted(elves, reverse=True)[0]}')
print(f'Top 3 elfs: {sum(sorted(elves, reverse=True)[0:3])}')
