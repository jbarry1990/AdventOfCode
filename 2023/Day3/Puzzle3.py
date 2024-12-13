import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content
def InRange(coord, h, w):
    if coord[0] <= h-1 and coord[0] >= 0 and coord[1] <= w-2 and coord[1] >=0:
        return True
    return False

def PartASolve(file_contents):
    Map = file_contents
    map_width = len(Map[0])
    map_height = len(Map)
    parts = []
    current_number = 0
    IsPart = False
    for r in range(map_height):
        for c in range(map_width):
            if c < map_width-1 and Map[r][c].isdigit():
                current_number = current_number*10+int(Map[r][c])
                for rd in [-1,0,1]:
                    for cd in [-1,0,1]:
                        if 0 <= r+rd < map_height and 0 <=c+cd < map_width-1:
                            if not Map[r+rd][c+cd].isdigit() and Map[r+rd][c+cd] != ".":
                                IsPart = True

            elif current_number > 0:
                if IsPart:
                    parts.append(current_number)
                    IsPart = False
                current_number = 0
    return sum(parts)                                                                     
                
def PartBSolve(file_contents):
    Map = file_contents
    map_width = len(Map[0])
    map_height = len(Map)
    gears = set()
    part_nums = dict()
    current_number = 0
    for r in range(map_height):
        for c in range(map_width):
            if c < map_width-1 and Map[r][c].isdigit():
                current_number = current_number*10+int(Map[r][c])
                for rd in [-1,0,1]:
                    for cd in [-1,0,1]:
                        if 0 <= r+rd < map_height and 0 <=c+cd < map_width-1:
                            if Map[r+rd][c+cd] =="*":
                                gears.add((r+rd,c+cd))

            elif current_number > 0:
                for gear in gears:
                    if gear in part_nums:
                        part_nums[gear].append(current_number)
                    else:
                        part_nums[gear] = [current_number]
                current_number = 0
                gears = set()
    answer = 0
    for k,v in part_nums.items():
        if len(v)==2:
            answer+= v[0]*v[1]
    return answer

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
