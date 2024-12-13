def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    number_of_positions = len(file_contents[0].strip("\n"))
    gamma = ""
    epsilon = ""
    for position in range(number_of_positions):
        Zeroes = 0
        Ones = 0
        for line in file_contents:
            if line[position] == "0":
                Zeroes = Zeroes + 1
            else:
                Ones = Ones + 1

        if Ones > Zeroes:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    
    return gamma * epsilon

def PartBSolve(file_contents):
    number_of_positions = len(file_contents[0].strip("\n"))
    OxygenRatingList = file_contents.copy()
    CO2RatingList = file_contents.copy()
    for position in range(number_of_positions):
        Zeroes = 0
        Ones = 0
        for line in OxygenRatingList:
            if line[position] == "0":
                Zeroes = Zeroes + 1
            else:
                Ones = Ones + 1
        lines_to_remove = []
        if Ones >= Zeroes:
            for index, line in enumerate(OxygenRatingList):
                if line[position] == "0":
                    lines_to_remove.append(index)
        else:
            for index, line in enumerate(OxygenRatingList):
                if line[position] == "1":
                    lines_to_remove.append(index)

        for line in reversed(lines_to_remove):
            OxygenRatingList.pop(line)
    
        if len(OxygenRatingList) == 1:
            break

    OxygenRating = int(OxygenRatingList[0], 2)

    for position in range(number_of_positions):
        Zeroes = 0
        Ones = 0
        for line in CO2RatingList:
            if line[position] == "0":
                Zeroes = Zeroes + 1
            else:
                Ones = Ones + 1
        lines_to_remove = []
        if Ones >= Zeroes:
            for index, line in enumerate(CO2RatingList):
                if line[position] == "1":
                    lines_to_remove.append(index)
        else:
            for index, line in enumerate(CO2RatingList):
                if line[position] == "0":
                    lines_to_remove.append(index)

        for line in reversed(lines_to_remove):
            CO2RatingList.pop(line)
    
        if len(CO2RatingList) == 1:
            break

    CO2Rating = int(CO2RatingList[0], 2)
    return OxygenRating * CO2Rating


def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
