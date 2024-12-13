def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    right_list = []
    left_list = []
    for line in file_contents:
        left,right = line.split("   ")
        right_list.append(int(right.strip()))
        left_list.append(int(left.strip()))

    left_list.sort()
    right_list.sort()

    sums = []
    for l,r in zip(left_list,right_list):
        sums.append(abs(l-r))
    
    return sum(sums)

def PartBSolve(file_contents):
    right_list = []
    left_list = []
    for line in file_contents:
        left,right = line.split("   ")
        right_list.append(int(right.strip()))
        left_list.append(int(left.strip()))

    sums = []
    for num in left_list:
        count = right_list.count(num)
        sums.append(num*count)

    return sum(sums)


def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
