def main():
    inputLines =  open("input.txt", "r").read()

    elfTotalCalories = []
    
    for elfInv in inputLines.split("\n\n"):
        currentElfInv = [int(x) for x in elfInv.strip().split("\n")]
        elfTotalCalories.append(sum(currentElfInv))
    print(f'Part one: {max(elfTotalCalories)}')
    
    elfTotalCalories.sort(reverse=True)

    print(f'Part two: {sum(elfTotalCalories[:3])}')

if __name__ == "__main__":
    main()
