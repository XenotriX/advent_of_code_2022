def print_screen(screen):
    for row in range(6):
        print(''.join(screen[row * 40:row * 40 + 40]))


with open('input.txt', 'r') as f:
    cycle = 1
    reg_x = 1
    fetch = True
    current_operation: int = 0
    sum = 0
    screen = [''] * 240

    while cycle <= 240:
        if abs(reg_x - ((cycle - 1) % 40)) <= 1:
            screen[cycle - 1] = '#'
        else:
            screen[cycle - 1] = '.'

        if fetch:
            line = f.readline()
            if not line:
                continue
            if line.strip() == 'noop':
                pass
            else:
                fetch = False
                current_operation = int(line.strip().split(' ')[1])
        else:
            fetch = True
            reg_x += current_operation

        cycle += 1

        if (cycle - 20) % 40 == 0:
            sum += cycle * reg_x


    print(f'(1) Sum {sum}')
    print('(2) Screen:')
    print_screen(screen)


