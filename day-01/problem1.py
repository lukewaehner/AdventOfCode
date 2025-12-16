def solve(input):
    zeroCount = 0
    currentNum = 50
    magnitudes = convertToMagnitude(input)

    for dir, magnitude in magnitudes:
        currentNum = processTurn(currentNum, dir, magnitude)
        # Apply rotation, increment for each time we hit zero
        if currentNum == 0:
            zeroCount += 1
    print("Zero count:", zeroCount)

# Convert raw string to (L, N) or (R, N) tuples
def convertToMagnitude(rawStr):
    magnitudes = []
    for line in rawStr.strip().split("\n"):
            dir = line.strip()[0]
            magnitude = int(line.strip()[1:])
            magnitudes.append((dir, magnitude))
    return magnitudes

def processTurn(currentNum, dir, magnitude):
    if dir == 'L':
        currentNum = (currentNum - magnitude)
        # If we overshot, wrap backaround
        if currentNum < 0:
            currentNum %= 100
    if dir == 'R':
        currentNum = (currentNum + magnitude)
        if currentNum >= 100:
            currentNum %= 100
    return currentNum

if __name__ == "__main__":
    # Grab input from file
    fp = "input.txt"
    with open(fp, "r") as f:
        input = f.read()

    # Given input
    testInput = """
                L68
                L30
                R48
                L5
                R60
                L55
                L1
                L99
                R14
                L82
                """
    # solve(testInput)
    solve(input)
