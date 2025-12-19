with open("input.txt") as f:
    lines = f.read()

testInput = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

grid = [list(row) for row in lines.splitlines()]
rows = len(grid)
cols = len(grid[0])


def mutateGrid(grid) -> int:
    removeable = 0
    for r in range(rows):
        for c in range(cols):
                    if grid[r][c] != "@":
                        continue
                    adj = 0
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue  # don't count self
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == "@":
                                    adj += 1

                    if adj < 4:
                        removeable += 1
                        grid[r][c] = 'x'  # remove it 
    return removeable

def main():
    totalRemoved = 0
    canRemove = True
    while canRemove:
        removed = mutateGrid(grid)
        if removed == 0:
            canRemove = False
        totalRemoved += removed 
    print(totalRemoved)
