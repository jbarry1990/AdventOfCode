def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    positions = file_contents[0].split(",")
    for index, position in enumerate(positions):
        positions[index] = int(position)

    return positions

def PartASolve(positions):
    minimum_fuel = 1000000
    for position in positions:
        prime = position
        fuel = 0
        for secondary_position in positions:
            fuel += abs(secondary_position - prime)
        if fuel < minimum_fuel:
            minimum_fuel = fuel            
            
    return minimum_fuel

def PartBSolve(positions):
    minimum_fuel = 1000000000
    positions.sort()
    lower_bound = positions[0]
    upper_bound = positions[-1]
    
    for position in range(lower_bound, upper_bound+1):
        prime = position
        fuel = 0
        for secondary_position in positions:
            distance = abs(secondary_position - prime)
            for step in range(1,distance+1):
                fuel += step
        if fuel < minimum_fuel:
            minimum_fuel = fuel            
            
    return minimum_fuel

def main():
    file_contents = ReadFile("Inputs.txt")
    positions = ParseFile(file_contents)
    answer = PartASolve(positions)
    print("Part A Answer: ", answer)
    answer = PartBSolve(positions)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
