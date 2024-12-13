from collections import defaultdict

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def PartASolve(inputs):
    Final = []
    Spaces = []
    position = 0
    file_id = 0
    Files = []

    for i,data in enumerate(inputs[0].strip()):
        if i%2 == 0:
            for x in range(int(data)):
                Final.append(file_id)
                Files.append((position,file_id))
                position +=1
            file_id +=1
        else:
            for x in range(int(data)):
                Final.append(None)
                Spaces.append(position)
                position +=1
                
    for file_pos,_id in reversed(Files):
        if len(Spaces) > 0:
            space_pos = Spaces.pop(0)
            if file_pos > space_pos:
                Final[space_pos] = _id
                Final[file_pos] = None
        else:
            break

    check_sum = 0
    for i,_id in enumerate(Final[0:len(Files)]):
        check_sum += (i*_id)

    return check_sum
        

def PartBSolve(inputs):
    Final = []
    Spaces = []
    position = 0
    file_id = 0
    Files = []

    for i,data in enumerate(inputs[0].strip()):
        if i%2 == 0:
            
            Files.append((position, int(data),file_id))
            for x in range(int(data)):
                Final.append(file_id)
                position +=1
            file_id +=1
        else:
            Spaces.append((position,int(data)))
            for x in range(int(data)):
                Final.append(None)
                position +=1
                
    for file_pos,file_size, _id in reversed(Files):
        for space_i,(space_pos,space_size) in enumerate(Spaces):
            if file_pos > space_pos and file_size <= space_size:
                for i in range(file_size):
                    Final[space_pos+i] = _id
                    Final[file_pos+i] = None
                Spaces[space_i] = (space_pos+file_size,space_size-file_size)
                break

    check_sum = 0
    for i,_id in enumerate(Final):
        if _id != None:
            check_sum += (i*_id)

    return check_sum

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
