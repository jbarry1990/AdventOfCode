import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    instructions = [x.split() for x in file_contents]
    instructions = [[x,int(y),z] for x,y,z in instructions]
    current = (0,0)
    positions = [current]
    boundaries = 0
    for instruction in instructions:
        boundaries += instruction[1]
        r,c = current
        if instruction[0] == "U":
            current = (r-1*instruction[1],c)
            positions.append(current)
        elif instruction[0] == "D":
            current = (r+1*instruction[1],c)
            positions.append(current)
        elif instruction[0] == "L":
            current = (r,c-1*instruction[1])
            positions.append(current)
        elif instruction[0] == "R":
            current = (r,c+1*instruction[1])
            positions.append(current)

    Area = abs(sum(positions[i][0]*(positions[i-1][1]-positions[(i+1)%len(positions)][1]) for i in range(len(positions))))//2
    interior = Area-boundaries//2+1
    return interior+boundaries
            
def PartBSolve(file_contents):        
    instructions = [x.split() for x in file_contents]
    instructions = [[int(z[2:-2],16),int(z[-2])] for x,y,z in instructions]
                    
    current = (0,0)
    positions = [current]
    boundaries = 0
    for instruction in instructions:
        boundaries += instruction[0]
        r,c = current
        if instruction[1] == 3:
            current = (r-1*instruction[0],c)
            positions.append(current)
        elif instruction[1] == 1:
            current = (r+1*instruction[0],c)
            positions.append(current)
        elif instruction[1] == 2:
            current = (r,c-1*instruction[0])
            positions.append(current)
        elif instruction[1] == 0:
            current = (r,c+1*instruction[0])
            positions.append(current)

    Area = abs(sum(positions[i][0]*(positions[i-1][1]-positions[(i+1)%len(positions)][1]) for i in range(len(positions))))//2
    interior = Area-boundaries//2+1
    return interior+boundaries

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
