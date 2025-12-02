def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
    return content

def PartASolve(inputs):
    patterns = inputs.split("\n\n")[0].split(", ")
    combos  = inputs.split("\n\n")[1].split("\n")
    seen = dict()

    def Solve(design):
        if len(design) == 0:
            return 1
        
        if design in seen:
            return seen[design]
        
        count = 0
        for p in patterns:
            if design.startswith(p):
                count = Solve(design[len(p):])
                if count != 0:
                    break
        seen[design] = count
        return count
    
    total = 0
    for combo in combos:
        total += Solve(combo)
    return total

def PartBSolve(inputs):
    patterns = inputs.split("\n\n")[0].split(", ")
    combos  = inputs.split("\n\n")[1].split("\n")
    seen = dict()
    
    def Solve(design):
        if len(design) == 0:
            return 1

        if design in seen:
            return seen[design]
        
        count = 0
        for p in patterns:
            if design.startswith(p):
                count += Solve(design[len(p):])
        seen[design]=count
        return count
    
    total = 0
    for combo in combos:
        total += Solve(combo)
    return total

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
