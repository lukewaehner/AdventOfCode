def solve(input):
    zeroCount = 0
    currentNum = 50
    magnitudes = convertToMagnitude(input)

    for dir, magnitude in magnitudes:
        print(f"Current number: {currentNum}, moving {dir}{magnitude}")
        tZC = zeroCount
        (currentNum, zeroCount) = processTurn(currentNum, dir, magnitude, zeroCount)
        if tZC != zeroCount: 
            print(f"Zero count updated: {tZC} -> {zeroCount}")
    print("Zero count:", zeroCount)

# Convert raw string to (L, N) or (R, N) tuples
def convertToMagnitude(rawStr):
    magnitudes = []
    for line in rawStr.strip().split("\n"):
            dir = line.strip()[0]
            magnitude = int(line.strip()[1:])
            magnitudes.append((dir, magnitude))
    return magnitudes

def processTurn(currentNum, dir, magnitude, zeroCount):
    if dir == 'L':
        # If we were at zero, can't rely on negatives and integer division
        invertOneRot = 0
        if currentNum == 0:
            invertOneRot = -1
        currentNum = (currentNum - magnitude)
        if currentNum < 0:
            zeroCount += abs((currentNum - 1) // 100) + invertOneRot
            currentNum %= 100
        elif currentNum == 0:
            zeroCount += 1
    if dir == 'R':
        currentNum = (currentNum + magnitude)
        if currentNum >= 100:
            # amount of times we crossed zero
            zeroCount += (currentNum  // 100)
            # bring it back into range
            currentNum %= 100
    return currentNum, zeroCount

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
