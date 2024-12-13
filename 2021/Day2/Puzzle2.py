def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    depth = 0
    distance = 0
    for line in file_contents:
        directions = line.split()
        if directions[0] == "forward":
            distance = distance + int(directions[1])
        if directions[0] == "up":
            depth = depth - int(directions[1])
        if directions[0] == "down":
            depth = depth + int(directions[1])

    return depth * distance

def PartBSolve(file_contents):
    depth = 0
    distance = 0
    aim = 0
    for line in file_contents:
        directions = line.split()
        if directions[0] == "forward":
            distance = distance + int(directions[1])
            depth = depth + (aim * int(directions[1]))
        if directions[0] == "up":
            aim = aim - int(directions[1])
        if directions[0] == "down":
            aim = aim + int(directions[1])

    return depth * distance   

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
