import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content

def Evaluate(key,part):
    x,m,a,s = part
    conditions = work[key]
    conditions = conditions.split(",")
    for condition in conditions:
        temp = condition.split(":")
        if len(temp) == 1:
            return temp[0]
        else:
             if eval(temp[0]):
                 return temp[1]

def PartASolve(file_contents):
    work_flows = file_contents[0:file_contents.index("")]
    parts = file_contents[file_contents.index("")+1:]
    parts = [x[1:-1] for x in parts]
    
    global work
    work = {}
    for work_flow in work_flows:
        x = work_flow.split("{")
        work[x[0]] = x[1][:-1]

    parts = [x.split(",") for x in parts]
    parts = [[int(y[2:]) for y in x] for x in parts]

    accepted = []
    for part in parts:
        current = "in"
        while True:
            current = Evaluate(current,part)

            if current == "A":
                accepted.append(part)
                break
            elif current == "R":
                break
             
    answer = 0
    for a in accepted:
        for x in a:
            answer +=x
    return answer

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
            
    return total

def PartBSolve(file_contents):
    global workflows
    workflows={}
    block1 = file_contents[0:file_contents.index("")]
    for line in block1:
        name,rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([],rules.pop())

        for rule in rules:
            comparison,target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key,cmp,n,target))

    answer = count({key: (1, 4000) for key in "xmas"})
            
    return answer

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
