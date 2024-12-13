def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    nums = []
    first_num = None
    last_num = None
    for line in file_contents:
        for char in line:
            if char.isnumeric():
                first_num = int(char)
                break
        for char in line[::-1]:
            if char.isnumeric():
                last_num = int(char)
                break
        nums.append(first_num*10+last_num)

    return sum(nums)

def PartBSolve(file_contents):
    nums = []
    for line in file_contents:
        first_num = None
        first_num_index = -1
        last_num = None
        last_num_index = -1
        for index, char in enumerate(line):
            if char.isnumeric():
                if first_num is None:
                    first_num = int(char)
                    first_num_index = index
                last_num = int(char)
                last_num_index = index

        if first_num == None:
            first_num_index = len(line)
            last_num_index = 0
        alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

        if first_num_index >= 3 or len(line)-last_num_index >=3:
            for num in alpha:
                first_res = line.find(num,0,first_num_index+1)
                last_res = line.rfind(num,last_num_index)
                if first_res != -1 and first_res < first_num_index:
                    first_num = alpha.index(num)+1
                    first_num_index = first_res
                if last_res != -1 and last_res > last_num_index:
                    last_num = alpha.index(num)+1
                    last_num_index = last_res

        nums.append(first_num*10+last_num)
    print(nums)
    return sum(nums)


def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
