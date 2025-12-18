with open('input.txt', 'r') as f:
    input = f.read()

testInput = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

# Data parsing
ranges, available = input.strip().split("\n\n")

# Combine all ranges to reduce total checks
def combineRanges(ranges):
    totalRanges = []
    ranges = ranges.splitlines()
    for r in ranges:
        start, end = map(int, r.split("-"))
        totalRanges.append((start, end))
        totalRanges = sorted(totalRanges, key=lambda x: x[0])
    totalRanges = mergeIntervals(totalRanges)
    return totalRanges


# Merge overlapping intervals together
def mergeIntervals(intervals):
    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged

totalRanges = combineRanges(ranges)

def checkRotten(available, totalRanges):
    totalFreshItems = 0
    for item in available:
        item = int(item)
        for r in totalRanges:
            if r[0] <= item <= r[1]:
                totalFreshItems += 1
                break
    print(totalFreshItems)

checkRotten(available.splitlines(), totalRanges)
