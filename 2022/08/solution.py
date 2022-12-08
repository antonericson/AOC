import time
import numpy as np
import matplotlib.pyplot as plt

def main():
    with open("input.txt", "r") as file:
        input = [line.strip() for line in file.readlines()]
        st1 = time.time()
        solve_one(input)
        et1 = time.time()
        print(f'Part one solved in: {print_time(st1, et1)}')

        st2 = time.time()
        solve_two(input)
        et2 = time.time()
        print(f'Part two solved in: {print_time(st2, et2)}')

def solve_one(input):
    # Build 2d array
    trees = []
    for y, row in enumerate(input):
        trees.append([])
        for tree in row:
            trees[y].append(int(tree))
    plotTrees = trees
    minY = 0
    minX = 0
    maxY = len(trees)-1
    treesVisible = 0
    for y, treeRow in enumerate(trees):
        maxX = len(treeRow)-1
        if y == 0 or y == maxY:
            continue
        for x, tree in enumerate(treeRow):
            if x == 0 or x == maxX:
                continue
            visibleUp, visibleDown, visibleRight, visibleLeft = True, True, True, True
            
            for xToCheck in range(x, maxX+1):
                if xToCheck == x:
                    continue
                if trees[y][xToCheck] >= tree:
                    visibleRight = False
                    break
            for xToCheck in reversed(range(minX, x)):
                if xToCheck == x:
                    continue
                if trees[y][xToCheck] >= tree:
                    visibleLeft = False
                    break
        
            for yToCheck in range(y, maxY+1):
                if yToCheck == y:
                    continue
                if trees[yToCheck][x] >= tree:
                    visibleDown = False
                    break;
            for yToCheck in reversed(range(minY, y)):
                if yToCheck == y:
                    continue
                if trees[yToCheck][x] >= tree:
                    visibleUp = False
                    break;
            if visibleUp or visibleDown or visibleLeft or visibleRight:
                plotTrees[y][x] = 10
                treesVisible += 1
                
    treesVisible += (len(trees)*2) + (len(trees[0]*2)) - 4

    H = np.array(plotTrees)
    fig = plt.figure(3)
    plt.imshow(H, interpolation='bicubic')
    plt.colorbar(orientation='vertical')
    plt.savefig('tree_map_part_1.png')
    plt.close()
    
    
    print(f'Part one: {treesVisible}')
    return # Return nothing, print results before this

def solve_two(input):
    # Build 2d array
    trees = []
    for y, row in enumerate(input):
        trees.append([])
        for tree in row:
            trees[y].append(int(tree))
    plotTrees = trees
    minY = 0
    minX = 0
    maxY = len(trees)-1
    maxScenicScore = 0
    for y, treeRow in enumerate(trees):
        scenicScore = 0
        maxX = len(treeRow)-1
        if y == 0 or y == maxY:
            continue
        for x, tree in enumerate(treeRow):
            if x == 0 or x == maxX:
                continue
            viewUp, viewDown, viewRight, viewLeft = 0, 0, 0, 0
            
            for xToCheck in range(x, maxX+1):
                if xToCheck == x:
                    continue
                viewRight += 1
                if trees[y][xToCheck] >= tree:
                    break
            for xToCheck in reversed(range(minX, x)):
                if xToCheck == x:
                    continue
                viewLeft += 1
                if trees[y][xToCheck] >= tree:
                    break
        
            for yToCheck in range(y, maxY+1):
                if yToCheck == y:
                    continue
                viewDown += 1
                if trees[yToCheck][x] >= tree:
                    break;
            for yToCheck in reversed(range(minY, y)):
                if yToCheck == y:
                    continue
                viewUp += 1
                if trees[yToCheck][x] >= tree:
                    break;
            scenicScore = viewDown * viewUp * viewLeft * viewRight
            plotTrees[y][x] = viewDown * viewUp * viewLeft * viewRight
            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore

        H = np.array(plotTrees)
        fig = plt.figure(figsize=(5, 5), frameon=False)
        plt.imshow(H)
        plt.colorbar(orientation='vertical')
        plt.savefig('tree_map_part_2.png')
        plt.close()

    print(f'Part two: {maxScenicScore}')
    return # Return nothing, print results before this

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'

if __name__ == "__main__":
    main()

