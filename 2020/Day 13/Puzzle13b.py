"""
Puzzle #13a - AdventOfCode
Read in bus scedule
determine t offset of each active bus
find a t where all buses leave on their t offset
example bus 1 leaves at t and bus 10 leaves at t+3 the earliest time stamp where both leave is 10
"""
from sympy.ntheory.modular import solve_congruence
def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Schedule = []

    for Entry in File:
        Schedule.append(Entry.strip())
            
    return Schedule

def DetermineActiveBusesSchedule(Schedule):
    ArrivalTime = int(Schedule[0])
    ActiveBuses = [(-TOffset, int(ActiveBus)) for TOffset, ActiveBus in enumerate(Schedule[1].split(",")) if ActiveBus != "x" ]
    return ActiveBuses

def main():
    Schedule = ReadInFile()
    ActiveBuses = DetermineActiveBusesSchedule(Schedule)
    TimeStamp = solve_congruence(*ActiveBuses)[0]
    print("Part 2: ", TimeStamp)

if __name__ == "__main__":
    main()
