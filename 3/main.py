with open('input.txt') as f:
    score = 0

    while line := f.readline():
        chars = list(line.strip())
        length = len(chars)
        left = set(chars[:int(length / 2)])
        right = set(chars[int(length / 2):])
        intersection = left.intersection(right)
        char = list(intersection)[0]
        if char.isupper():
            score += ord(char) - 65 + 27
        else:
            score += ord(char) - ord('a') + 1

    print(f'(1) The sum of all the overlaps is: {score}')

with open('input.txt') as f:
    score = 0

    while line1 := f.readline():
        line2 = f.readline()
        line3 = f.readline()

        elf1 = set(line1.strip())
        elf2 = set(line2.strip())
        elf3 = set(line3.strip())

        intersection1 = elf1.intersection(elf2)
        intersection2 = intersection1.intersection(elf3)

        assert len(intersection2) == 1

        char = list(intersection2)[0]
        if char.isupper():
            score += ord(char) - 65 + 27
        else:
            score += ord(char) - ord('a') + 1

    print(f'(2) The sum of all the badges is: {score}')
