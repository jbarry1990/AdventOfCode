def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    fish_list = file_contents[0].split(",")
    for index, fish in enumerate(fish_list):
        fish_list[index] = int(fish)

    return fish_list

def PartASolve(fish_list, days):
    final_list = fish_list.copy()

    #decrement list if number is 0 reset to 6
    #add 8 to the end of the list for every number that was reset to 6
    #run for specified number of days and return the number of fish at the end
    count = 0
    while count != days:
        new_spawn = 0
        for index, fish in enumerate(final_list):
            if fish ==0:
                final_list[index] = 6
                new_spawn +=1
                continue
            final_list[index] -=1

        for spawn in range(new_spawn):
            final_list.append(8)

        count +=1                
    return len(final_list)

def PartBSolve(fish_list, days):
    fish_age = {}

    for index in range(9):
        fish_age[index] = 0

    for fish in fish_list:
        fish_age[fish] +=1

    count = 0
    while count != days:
        new_fish = fish_age[0]
        fish_age[0] = fish_age[1]
        fish_age[1] = fish_age[2]
        fish_age[2] = fish_age[3]
        fish_age[3] = fish_age[4]
        fish_age[4] = fish_age[5]
        fish_age[5] = fish_age[6]
        fish_age[6] = fish_age[7] + new_fish
        fish_age[7] = fish_age[8]
        fish_age[8] = new_fish

        count +=1
    total_fish = 0
    for key in fish_age:
        total_fish += fish_age[key]
    return total_fish

def main():
    file_contents = ReadFile("Inputs.txt")
    fish_list = ParseFile(file_contents)
    answer = PartASolve(fish_list, 80)
    print("Part A Answer: ", answer)
    answer = PartBSolve(fish_list, 256)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
