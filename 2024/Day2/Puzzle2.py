def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content
    
def Check(num_array):
    safe = True
    for i in range(1, len(num_array)):
        if num_array[i] > num_array[i-1] and 0 < abs(num_array[i] - num_array[i-1]) <=3:
            continue
        safe = False
        break
        
    if not safe:
        for i in range(1, len(num_array)):
            if num_array[i] < num_array[i-1] and 0 < abs(num_array[i] - num_array[i-1]) <=3:
                continue
            return safe
        safe = True
    return safe

def PartASolve(file_contents):
    count = 0
    for line in file_contents:
        arr = [int(x) for x in line.split(" ")]
        IsSafe = Check(arr)
        if IsSafe:
            count +=1
    return count
    

def PartBSolve(file_contents):
    count = 0
    for line in file_contents:
        arr = [int(x) for x in line.split(" ")]
        IsSafe = Check(arr)
        if IsSafe:
            count +=1
        else:
            for i in range(0,len(arr)):
                temp = arr.copy()
                temp.pop(i)
                IsSafe = Check(temp)
                if IsSafe:
                    count +=1
                    break
    return count

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
