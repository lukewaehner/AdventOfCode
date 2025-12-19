with open('input.txt', 'r') as f:
    input = f.read()
testInput = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def solve():
    # Prep problems
    grid = [list(line) for line in input.splitlines()]
    rows = len(grid)
    cols = max(len(row) for row in grid)
    problems = [[]]
    problemNum = 0
    for c in range(cols - 1, -1, -1):
        # Skip empty columns
        curr = 0
        for r in range(rows):
            if c < len(grid[r]):
                if grid[r][c].isdigit():
                    curr = curr * 10 + int(grid[r][c])
                # Marks end of a problem, save token, signal new problem, add space, reset
                elif grid[r][c] in ('*', '+'):
                    problems[problemNum].append(curr)
                    curr = 0
                    problems[problemNum].append(grid[r][c])
                    problemNum += 1
                    # Add space only if its not the last problem
                    if c != 0:
                        problems.append([])
            else: 
                pass
        if curr != 0:
            # Save on EOL
            problems[problemNum].append(curr)
    print(problems)


    # Solve for total sum of problems
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

solve()
