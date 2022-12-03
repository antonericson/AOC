import time

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
        print(f'Part one solved in: {print_time(st2, et2)}')

def solve_one(input):
    backpacks = input
    
    totalSum = 0
    for backpack in backpacks:
        compartment_one, compartment_two = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
        common_item = ''.join(set(compartment_one).intersection(compartment_two))
        totalSum += (ord(common_item) & 31)
        if common_item.isupper():
            totalSum += 26

    print(f'Part one: {totalSum}')
    return # Return nothing, print results before this

def solve_two(input):
    backpacks = input
    done = False
    totalSum = 0
    
    si, ei = 0, 3
    while(not done):
        backpack_one, backpack_two, backpack_three = backpacks[si:ei]
        tmp = ''.join(set(backpack_one).intersection(backpack_two))
        badge = ''.join(set(tmp).intersection(backpack_three)).strip()
        
        totalSum += (ord(badge) & 31)
        if badge.isupper():
            totalSum += 26
            
        if ei == len(backpacks):
            done = True
        else:
            si += 3
            ei += 3
    
    
    
    print(f'Part two: {totalSum}')
    return # Return nothing, print results before this


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

