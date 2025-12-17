with open("input.txt", "r") as f:
    input = f.read()

# input = """
#         987654321111111
#         811111111111119
#         234234234234278
#         818181911112111
#         """

# input = "818181911112111"

# verbose = True 
verbose = False
totalVoltage = 0

for line in input.split():
    if verbose:
        print(f"Processing line: {line}")
    currentConsumedBatteries = 0 # Max 12
    lastUsedIndex = -1
    voltageStr = "" # Add biggest digits
    if (len(line) < 12):
        break # Bad line
    elif (len(line) == 12):
        totalVoltage += int(line)
        continue # Entire line is the best we can do 

    # Needs 12 digits, pick the largest one that leaves 11 digits after it, then 10, etc 
    while (currentConsumedBatteries < 12):
        # Tracks for best
        biggestDigit = -1
        biggestDigitIndex = -1
        # Scan slices of the array that leave enough room for remaining digits needed
        for i in range(lastUsedIndex + 1, len(line) - (12 - currentConsumedBatteries - 1)):
            currentDigit = int(line[i])
            if verbose:
                print(f"Considering {currentDigit} against {biggestDigit}")
            if (currentDigit > biggestDigit):
                # Save the best diit and index
                biggestDigit = currentDigit
                biggestDigitIndex = i
        if verbose:
            # Best pick this slice
            print(f"Picked: {biggestDigit} in {line[lastUsedIndex+1:(len(line) - (12 - currentConsumedBatteries)) + 1]}")
        voltageStr += str(biggestDigit)
        # Move to next index in string
        lastUsedIndex = biggestDigitIndex
        # Track that we found another battery
        currentConsumedBatteries += 1
    totalLineVoltage = int(voltageStr)
    totalVoltage += totalLineVoltage
print(f"Total voltage: {totalVoltage}")

