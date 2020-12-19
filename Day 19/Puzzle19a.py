"""
Puzzle #19a - AdventOfCode
1. Read Rules and Data in
2. Using itertools determine all combinations of rules for rule set.
3. Determine if the messages match any of the rule combinations
4. Output the sum of valid messages
"""
  
from time import time
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

def main():
    t_start = time()
    
    Rules, Data = ReadInFile()
    ValidMessages = set(Solve(0,Rules))
    Answer = sum(Matches in ValidMessages for Matches in Data)
    print("Part 1", Answer)

    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
