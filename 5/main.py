# open the file and read its contents
with open("input.txt", "r") as f:
    lines = []
    # read each line from the file
    for line in f:
        print('line: ', line)
        # if the line is empty, stop reading
        if line[0] == '\n':
            lines.pop()
            break
        # otherwise, add the line to the list
        lines.append(line)

    # The remaining lines of the input contain the moves
    moves = f.readlines()

# Split the lines into individual elements
rows = []
for line in lines:
    # split the string by whitespace to get the individual characters
    chunks = [line[i:i+4].strip() for i in range(0, len(line), 4)]
    chunks = [''.join([char for char in c if char.isalpha()]) for c in chunks]
    rows.append(chunks)

# Convert the rows into stacks
stacks = [list(reversed(column)) for column in zip(*rows)]
stacks = [[char for char in stack if char != ''] for stack in stacks]
stacks2 = [list(stack) for stack in stacks]
print(stacks)

moves = [move.strip() for move in moves]

# Apply the moves to the stacks
for move in moves:
    print(move)
    chunks = move.split(' ')
    count = int(chunks[1])
    from_stack = int(chunks[3]) - 1
    to_stack = int(chunks[5]) - 1

    # Task 1 move
    for _ in range(count):
        val = stacks[from_stack].pop()
        stacks[to_stack].append(val)
        print('Task 1: ', stacks)

    # Task 2 move
    stacks2[to_stack].extend(stacks2[from_stack][-count:])
    del stacks2[from_stack][-count:]
    print('Task 2: ', stacks2)

# Print the top element of each stack
output = ''
for stack in stacks:
    output += stack.pop()

print(f'(1) Move single element: {output}')

output = ''
for stack in stacks2:
    output += stack.pop()

print(f'(2) Move mult. elements: {output}')
