import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content
    


def PartASolve(file_contents):
    solve = 0
    for line in file_contents:
        matches= re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', line)
        for match in matches:
            numbers = [int(match) for match in re.findall(r'\b([0-9]{1,3})\b', match)]
            solve += numbers[0]*numbers[1]
    return solve
    

def PartBSolve(file_contents):
    solve = 0
    line = "".join(file_contents)
    donts = [m.start() for m in re.finditer('don\'t\(\)', line)]
    dos = [m.start() for m in re.finditer('do\(\)', line)]
    check = True
    checking = True
    start = 0
    stop = donts[0]
    results = []
    while checking:
        if check:
            matches = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', line[start:stop])
            for match in matches:
                results.append(match)
            if stop == len(line):
                checking = False
            else:
                check = False
        else:
            found_start = False
            for num in dos:
                if num > stop:
                    start = num
                    check = True
                    break
            if start < stop:
                checking = False
            else:
                for num in donts:
                    if num > start:
                        stop = num
                        check = True
                        break

                if stop < start:
                    stop = len(line)
                    check = True
    for match in results:
            numbers = [int(match) for match in re.findall(r'\b([0-9]{1,3})\b', match)]
            solve += numbers[0]*numbers[1]
    return solve

                            
                    

    return

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
