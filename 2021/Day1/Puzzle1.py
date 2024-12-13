def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    NumberOfIncreases = 0

    for index, line in enumerate(file_contents):
        if index == 0:
            continue
        previous_number = int(file_contents[index-1])
        if previous_number < int(line):
            NumberOfIncreases = NumberOfIncreases + 1

    return NumberOfIncreases

def PartBSolve(file_contents):
    NumberOfIncreases = 0

    for index, line in enumerate(file_contents):
        if index < 3:
            continue
        previous_window = int(file_contents[index-3]) +\
                          int(file_contents[index-2]) +\
                          int(file_contents[index-1])
        current_window = int(line) +\
                         int(file_contents[index-2]) +\
                         int(file_contents[index-1])

        if previous_window < current_window:
            NumberOfIncreases = NumberOfIncreases + 1

    return NumberOfIncreases    

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
