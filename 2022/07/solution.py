import time

def main(): # new thread will get stack of such siz
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

def solve_one(lines):
    directories = getAllDirectories(lines)
    sum = 0
    knownDirs = {}
        
    for dir in directories:
        if dir in knownDirs.keys():
            directories[dir] = knownDirs[dir]
        else:
            directories[dir] = getDirSize(dir, directories, knownDirs)
            knownDirs[dir] = directories[dir]
        if directories[dir] <= 100000:
            sum += directories[dir]
    
    print(f'Part one: {sum}') # 1623729, 1488737 too low
    return # Return nothing, print results before this

def solve_two(lines):
    directories = getAllDirectories(lines)
    knownDirs = {}
    for dir in directories:
        if dir in knownDirs.keys():
            directories[dir] = knownDirs[dir]
        else:
            directories[dir] = getDirSize(dir, directories, knownDirs)
            knownDirs[dir] = directories[dir]

    directories = dict(sorted(directories.items(), key=lambda item: item[1]))

    totalDiskSpace = 70000000
    totalSpaceNeeded = 30000000
    spaceUsed = totalDiskSpace - directories['/']
    minSpaceToBeDeleted = totalSpaceNeeded - spaceUsed
    
    dirSizeToRemove = 0
    for dir in directories:
        if directories[dir] >= minSpaceToBeDeleted:
            dirSizeToRemove = directories[dir]
            break

    print(f'Part two: {dirSizeToRemove}')
    return # Return nothing, print results before this

def getAllDirectories(lines):
    directories = {}
    currentPath = '/'
    done = False
    i = 0

    while not done:
        if lines[i][0] != '$':
            #Error
            print(f'Expected command, got: {lines[i]}')
            return

        if 'cd' in lines[i]:
            moveTo = lines[i].split(' ')[2]
            if not moveTo == '/':
                if moveTo == '..':
                    currentPath = '|'.join(currentPath.split('|')[:-1])
                else:
                    currentPath += '|'+moveTo

        if 'ls' in lines[i]:
            i += 1
            while i < len(lines) and '$' not in lines[i]:
                size, name = lines[i].split(' ')
                if size != 'dir':
                    if currentPath in directories.keys():
                        directories[currentPath].append(int(size))
                    else:
                        directories[currentPath] = [int(size)]
                else:
                    if currentPath in directories.keys():
                        directories[currentPath].append(currentPath+'|'+name)
                    else:
                        directories[currentPath] = [currentPath+'|'+name]
                i += 1
        else:
            i += 1
        if i >= len(lines):
            done = True
            
    return directories

def getDirSize(dirName, directories, knownDirs):
    
    if all(isinstance(item, int) for item in directories[dirName]):
        knownDirs[dirName] = sum(directories[dirName])
        return sum(directories[dirName])
    
    sizes = [size for size in directories[dirName] if isinstance(size, int)]
    tmpSize = sum(sizes)
    
    dirsToCheck = [name for name in directories[dirName] if isinstance(name, str)]
    for dir in dirsToCheck:
        if dir in knownDirs.keys():
            tmpSize = tmpSize + knownDirs[dir]
        else:
            tmpSize = tmpSize + getDirSize(dir, directories, knownDirs)
        
    knownDirs[dirName] = tmpSize
    return tmpSize

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

