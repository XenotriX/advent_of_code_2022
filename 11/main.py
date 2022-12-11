import math
from tqdm import tqdm
from functools import reduce
from copy import deepcopy

class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.operation = ''
        self.test = None
        self.action_true = None
        self.action_false = None
        self.times_inspected = 0

    def __str__(self) -> str:
        return f'Items: {self.items}\n' + \
               f'Operation: {self.operation}\n' + \
               f'Test: Divisible by {self.test}\n' + \
               f'If true: throw to monkey {self.action_true}\n' + \
               f'If false: throw to monkey {self.action_false}\n' + \
               f'Times inspected: {self.times_inspected}'


current = None
monkeys = []

with open('input.txt', 'r') as f:
    while line := f.readline():
        line = line.strip()
        if line.startswith('Monkey'):
            current = Monkey()
            monkeys.append(current)
        elif line.startswith('Starting items'):
            current.items = line.split(': ')[1].split(', ')
            current.items = [int(item) for item in current.items]
        elif line.startswith('Operation'):
            current.operation = line.split(' = ')[1]
        elif line.startswith('Test'):
            current.test = int(line.split(' by ')[1])
        elif line.startswith('If true'):
            current.action_true = int(line.split('monkey ')[1])
        elif line.startswith('If false'):
            current.action_false = int(line.split('monkey ')[1])

def play_rounds(monkeys, rounds, div_by_3=False):
    lcm = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys])
    for round in tqdm(range(rounds)):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.times_inspected += 1
                old = item
                item = eval(monkey.operation)
                if div_by_3:
                    item /= 3
                item = math.floor(item)
                item %= lcm
                if item % monkey.test == 0:
                    monkeys[monkey.action_true].items.append(item)
                else:
                    monkeys[monkey.action_false].items.append(item)

    m1, m2 = sorted(monkeys, key=lambda m: m.times_inspected)[-2:]
    return m1.times_inspected * m2.times_inspected

task1 = play_rounds(deepcopy(monkeys), 20, div_by_3=True)
task2 = play_rounds(monkeys, 10000)

print(f'(1) Monkey business with relief: {task1}')
print(f'(2) Monkey business without relief: {task2}')

