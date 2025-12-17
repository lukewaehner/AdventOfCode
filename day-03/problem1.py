with open("input.txt", "r") as f:
    input = f.read()

# input = """
#         987654321111111
#         811111111111119
#         234234234234278
#         818181911112111
#         """

totalVoltage = 0

for line in input.split():
    best = (0, 0)
    # Greedy: Pick the biggest digit, that is not the last one
    # Duplicates do not overwrite the index we choose from, then pick the largest digit after
    for i in range(len(line) - 1):
        # Choose the biggest digit in the line that is not the last one
        if int(line[i]) > best[0]:
            best = (int(line[i]), i)
    followingBest = (0, 0) 
    for i in range(best[1] + 1, len(line)):
        if int(line[i]) > followingBest[0]:
            followingBest = (int(line[i]), i)
    # Combine the two digits to form the voltage of the given line
    totalLineVoltage = (best[0] * 10) + followingBest[0]
    # Save out
    totalVoltage += totalLineVoltage
    print(f"Best: {best[0]}, Following best: {followingBest[0]}, Line voltage: {totalLineVoltage}")
    print(f"Total voltage so far: {totalVoltage}")



