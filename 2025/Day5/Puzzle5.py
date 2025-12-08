def ReadInputs():
    File = open("./Inputs.txt", "r")
    File = File.read()
    ranges, items = File.split("\n\n")
        
    ranges = ranges.split()
    ranges = [r.split("-") for r in ranges]
    ranges = [[int(x),int(y)] for [x,y] in ranges]
    
    items = items.split()
    items = [int(x) for x  in items]

    return [ranges, items]
    
def solveA(Input):
    count = 0
    ranges, items = Input

    for item in items:
        for low,high in ranges:
            if low <= item <= high:
                count += 1
                break
    return count

def solveB(Input):
    ranges = Input[0]

    ranges.sort(key=lambda x:x[0])
    combined = []
    current_low = ranges[0][0]
    current_high = ranges[0][1]
    for x,[low,high] in enumerate(ranges):
        if x == len(ranges)-1:
            if low == current_low:
                combined.append([low,high])
            else:
                combined.append([current_low,high])
            break
        if ranges[x+1][0] - high <=1 or current_high == ranges[x+1][0]:
            current_high = max(ranges[x+1][1], current_high)
        else:
            combined.append([current_low, current_high])
            current_low = ranges[x+1][0]
            current_high = ranges[x+1][1]
    total = 0
    for low,high in combined:
        total += (high-low)+1


    return total     
    
def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
