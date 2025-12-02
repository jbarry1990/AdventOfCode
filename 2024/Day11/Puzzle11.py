from collections import defaultdict

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def PartASolve(inputs):
    starting = [int(x) for x in inputs[0].strip().split(" ")]
    stones = defaultdict(int)

    for x in starting:
        stones[x] = 1

    for _ in range(25):
        new_stones = defaultdict(int)
        stones_list = list(stones.keys())
        for stone in stones_list:
            count = stones[stone]

            if stone == 0:
                new_stones[stone+1] += count
            elif len(str(stone))%2 == 0:
                new_stones[int(str(stone)[0:len(str(stone))//2])] += count
                new_stones[int(str(stone)[len(str(stone))//2:])] += count
            else:
                new_stones[stone*2024] += count
        stones = new_stones
    total = 0
    for stone in stones:
        total += stones[stone]
    return total

def PartBSolve(inputs):
    starting = [int(x) for x in inputs[0].strip().split(" ")]
    stones = defaultdict(int)

    for x in starting:
        stones[x] = 1

    for _ in range(75):
        new_stones = defaultdict(int)
        stones_list = list(stones.keys())
        for stone in stones_list:
            count = stones[stone]

            if stone == 0:
                new_stones[stone+1] += count
            elif len(str(stone))%2 == 0:
                new_stones[int(str(stone)[0:len(str(stone))//2])] += count
                new_stones[int(str(stone)[len(str(stone))//2:])] += count
            else:
                new_stones[stone*2024] += count
        stones = new_stones
    total = 0
    for stone in stones:
        total += stones[stone]
    return total

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
