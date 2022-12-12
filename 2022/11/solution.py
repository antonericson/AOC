import time
import math
import string

def main():
    with open("input.txt", "r") as file:
        input = file.readlines()
        st1 = time.time()
        solve_one(input)
        et1 = time.time()
        print(f'Part one solved in: {print_time(st1, et1)}')


        st2 = time.time()
        solve_two(input)
        et2 = time.time()
        print(f'Part two solved in: {print_time(st2, et2)}')

def solve_one(input):
    input = [l.strip() for l in input]
    rounds = 20

    monkeys = getMonkeys(input)

    for round in range(1,rounds+1):
        for mi in range(0,len(monkeys)):
            items_to_remove = []
            for item_base_worry in monkeys[mi]['items']:
                monkeys[mi]['inspections'] += 1
                current_worry = monkeys[mi]['op'](item_base_worry)
                current_worry = math.floor(current_worry / 3)
                monkeys[monkeys[mi]['throw_to'](current_worry)]['items'].append(current_worry)
                items_to_remove.append(item_base_worry)
            for item in items_to_remove:
                monkeys[mi]['items'].remove(item)

    monkey_business = []
    for monkey in monkeys:
        monkey_business.append(monkey['inspections'])

    second_place, first_place = sorted(monkey_business)[-2:]


    print(f'Part one: {first_place * second_place}')
    return # Return nothing, print results before this

def solve_two(input):
    input = [l.strip() for l in input]
    rounds = 10000
    monkeys = getMonkeys(input)

    mod_factor = math.prod([monkey['div_by'] for monkey in monkeys])

    for round in range(1,rounds+1):
        for mi in range(0,len(monkeys)):
            items_to_remove = []
            for item_base_worry in monkeys[mi]['items']:
                monkeys[mi]['inspections'] += 1
                current_worry = monkeys[mi]['op'](item_base_worry)
                current_worry %= mod_factor
                monkeys[monkeys[mi]['throw_to'](current_worry)]['items'].append(current_worry)
                items_to_remove.append(item_base_worry)
            for item in items_to_remove:
                monkeys[mi]['items'].remove(item)

    monkey_business = []
    for monkey in monkeys:
        monkey_business.append(monkey['inspections'])

    second_place, first_place = sorted(monkey_business)[-2:]


    print(f'Part two: {first_place * second_place}')
    return # Return nothing, print results before this

def getMonkeys(input):
    monkeys = []
    current_monkey = {'inspections': 0}
    for i in range(0,len(input)):
        current_line = input[i]
        if not current_line:
            monkeys.append(current_monkey)
            current_monkey = {'inspections': 0}
        first_word = input[i].split(' ')[0]
        if 'Starting' in first_word:
            current_monkey['items'] = [int(w) for w in current_line.split(': ')[-1].split(', ')]
            continue
        if 'Operation' in first_word:
            current_monkey['op'] = eval(f'lambda old:{current_line.split(" = ")[-1]}')
            continue
        if 'Test' in first_word:
            divisible_by = int(current_line.split(' ')[-1])
            true_res = int(input[i+1].split(' ')[-1])
            false_res = int(input[i+2].split(' ')[-1])
            current_monkey['throw_to'] = eval(f'lambda w: {true_res} if w % {divisible_by} == 0 else {false_res}')
            current_monkey['div_by'] = divisible_by
            continue
    monkeys.append(current_monkey)
    return monkeys

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

