with open('input.txt', 'r') as f:
    input = f.read()
testInput = """123 328  51 64 
 45 64  387 23
  6 98  215 314
*   +   *   +  
"""

grid = [list(line.strip()) for line in input.splitlines()]
problems = [[]] # List of problems, each problem is a list of characters to be parsed later
for r in range(len(grid)):
    problemNum = 0
    print(f"Row {r}:")
    appendToNext = False
    c = 0
    currentNum = 0
    while c < len(grid[r]):
        if grid[r][c].isdigit():
            currentNum = currentNum * 10 + int(grid[r][c])
            # Advance out of bounds needs to save
            if c + 1 == len(grid[r]):
                problems[problemNum].append(currentNum)
            c += 1
        elif grid[r][c] == ' ':
            # Hit a space, store the number, move to next problem, create space, reset
            if currentNum != 0:
                problems[problemNum].append(currentNum)
            currentNum = 0
            problemNum += 1
            # Add space for new problem if needed
            if problemNum >= len(problems):
                problems.append([])
            while c < len(grid[r]) and grid[r][c] == ' ':
                # Advance until non-space
                c += 1
        elif grid[r][c] in ('*', '+'):
            # Hit operator, store the operator and continue
            problems[problemNum].append(grid[r][c])
            c += 1
        else:
            # Idk advance either way
            c += 1
print(problems)
print("Tokens:")

totalSum = 0
for problem in problems:
    if problem[-1] == '+':
        adding = True
        solution = 0
    else:
        adding = False
        solution = 1
    for token in range(len(problem)-1):
        if adding:
            solution += problem[token]
        if not adding:
            solution *= problem[token]
    totalSum += solution
print(totalSum)

