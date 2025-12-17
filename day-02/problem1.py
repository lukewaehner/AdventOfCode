def solution(verbose=False, testInput=None):
    if testInput:
        input = testInput
    else:
        with open('input.txt') as f:
            input = f.read()

    totalInvalidId = 0

    for line in input.split(','):
        (start, end) = (line.split('-'))
        print(f"Checking in range: {start}, {end}")
        currentHits = 0
        for i in range(int(start), int(end) + 1):
            i = str(i)
            if len(i) % 2 != 0:
               continue 
            if i[:len(i)//2] == i[len(i)//2:]:
                if verbose:
                    print(f"Found hit: {i}")
                else:
                    currentHits += 1
                totalInvalidId += int(i)
        if not verbose:
            print(f"Current hits in range: {currentHits}")
    print(totalInvalidId)



def test():
    for s in ["55", "1010", "123123", "12341234"]:
        print(s)
        print(s[:len(s)//2])
        print(s[len(s)//2:])
        if s[:len(s)//2] == s[len(s)//2:]:
            print("Good")


if __name__ == "__main__":
    # test()
    tIpt = """
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
        """
    solution()
