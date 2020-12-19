"""
Puzzle #19a - AdventOfCode
1. Read Rules and Data in
2. Using itertools determine all combinations of rules for rule set.
3. Determine if the messages match any of the rule combinations
4. Output the sum of valid messages
"""
  

import itertools

def ReadInFile():
    Rules = {}
    Data = []
    
    File = open("./PuzzleInput.txt", "r")
    
    Lines = []
    for Line in File:
        Lines.append(Line.strip())
        
    NewLine = Lines.index("")

    for Rule in Lines[:NewLine]:
        Key,Value = Rule.split(": ")
        Rules[int(Key)] = Value

    for Line in Lines[NewLine+1:]:
        Data.append(Line)

    return Rules, Data



def Solve(Key,Rules, Depth=0):
    if Depth > 10:
        return

    if '"' in Rules[Key]:
        yield Rules[Key][1:-1]
    else:
        for SubRules in Rules[Key].split(" | "):
            for Combination in itertools.product(*[Solve(int(Rule), Rules, Depth + 1) for Rule in SubRules.split()]):
                yield "".join(Combination)

def SolveNewRules(Rules, Data):
    Rules[8] = "42 | 42 8"
    Rules[11] = "42 31 | 42 11 31"

    first = set(Solve(42,Rules))
    second = set(Solve(31,Rules))
    part2 = 0
    k = [len(x) for x in first][0]
    assert(all(len(x) == k for x in first | second))
    for s in Data:
        if len(s) % k != 0:
            continue

        dp1 = [s[i:i+k] in first for i in range(0, len(s), k)]
        dp2 = [s[i:i+k] in second for i in range(0, len(s), k)]

        part2 += any(all(dp1[:i]) and all(dp2[i:]) and i > (len(dp1) - i) for i in range(len(dp1)))
    return part2
def main():
    Rules, Data = ReadInFile()
    Answer = SolveNewRules(Rules, Data)

    print("Part 2: ",Answer)
    
if __name__ == "__main__":
    main()
