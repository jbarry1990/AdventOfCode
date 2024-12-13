from more_itertools import distinct_permutations

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
def Validate(line,row,nums):

    #1. Check that known elements are the same
    for i, ch in enumerate(row):
        if ch == "#" and line[i] != "#":
            return False
        elif ch == "." and line[i] != ".":
            return False

    #2. If known elements are the right configuration, check the unknown
    line = line.replace("."," ")
    line = line.replace("?"," ")
    counts = [x.strip() for x in line.split()]

    if len(counts) != len(nums):
        return False
    for i,num in enumerate(nums):
        if counts[i].count("#") != num:
            return False

    return True
    
def PartASolve(file_contents):
##    valids = []
##    for line in file_contents:
##        row,nums = line.split(" ")
##        nums = [int(i) for i in nums.split(",")]
##        borked = sum(nums)
##        fixed = len(row)-borked
##        pattern = []
##        for i in range(borked):
##            pattern.append("#")
##        for i in range(fixed):
##            pattern.append(".")
##        perm = distinct_permutations(pattern)
##
##        perm = list(set(list(perm)))
##        perm = ["".join(i) for i in perm]
##
##        count = 0
##        for x,i in enumerate(perm):
##            if Validate(i,row,nums) == True:
##                count +=1
##
##        valids.append(count)
##
##    return sum(valids)
    total = 0
    for line in file_contents:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        
        total += count(cfg, nums)
    return total

cache = {}
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1
    
    key = (cfg, nums)
    
    if key in cache:
        return cache[key]

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result

def PartBSolve(file_contents):        
    total = 0

    for line in file_contents:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        
        cfg = "?".join([cfg] * 5)
        nums *= 5
        
        total += count(cfg, nums)
    return total

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
