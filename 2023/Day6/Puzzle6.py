import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    time = [int(n) for n in file_contents[0].split(":")[1].strip().split("     ")]
    distance = [int(n) for n in file_contents[1].split(":")[1].strip().split("   ")]
    races = [(t,distance[i]) for i,t in enumerate(time)]
    wins = []
    for t,d in races:
        count = 0
        for i in range(t):
            if i*(t-i) > d:
                count+=1
        wins.append(count)
        
    answer = 1
    for win in wins:
        answer*=win

    return answer

def PartBSolve(file_contents):
    time = [n for n in file_contents[0].split(":")[1].strip().split("     ")]
    distance = [n for n in file_contents[1].split(":")[1].strip().split("   ")]
    time = int("".join(time))
    distance = int("".join(distance))
    wins = 0
    for i in range(time):
        if i*(time-i) > distance:
            wins+=1
        
    return wins

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
