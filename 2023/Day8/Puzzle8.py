from math import lcm

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    directions = list(file_contents[0].strip())
    locations = {}
    for line in file_contents[2::]:
        key,value = line.split("=")
        key = key.strip()
        value = value.strip()[1:-1]
        value = value.split(",")
        locations[key] = (value[0].strip(), value[1].strip())

    current_location = "AAA"
    current_direction_index = 0
    count = 0
    while current_location != "ZZZ":
        #print("Starting Location: ", current_location)
        #print("Starting Direction: ", directions[current_direction_index])
        if directions[current_direction_index] == "L":
            current_location = locations[current_location][0]
        else:
            current_location = locations[current_location][1]

        if current_direction_index == len(directions)-1:
            current_direction_index = 0
        else:
            current_direction_index +=1
        count +=1
        #print("Next Location: ", current_location)
        #print("Next Direction: ", directions[current_direction_index])

    return count
        
def CheckStartingLocations(starting_locations):
    for location in starting_locations:
        if location[-1] != "Z":
            return False
    return True

def PartBSolve(file_contents):        
    directions = list(file_contents[0].strip())
    locations = {}
    starting_locations = []
    for line in file_contents[2::]:
        key,value = line.split("=")
        key = key.strip()
        value = value.strip()[1:-1]
        value = value.split(",")
        locations[key] = (value[0].strip(), value[1].strip())
        if key[-1] == "A":
            starting_locations.append(key)

    current_direction_index = 0
    loops = []
    for location in starting_locations:
        current_location = location
        count = 0
        while current_location.endswith("Z") != True:
            if directions[current_direction_index] == "L":
                current_location = locations[current_location][0]
            else:
                current_location = locations[current_location][1]

            if current_direction_index == len(directions)-1:
                current_direction_index = 0
            else:
                current_direction_index +=1
            count +=1
        loops.append(count)
    return lcm(loops[0],loops[1], loops[2],loops[3],loops[4],loops[5])
    

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
