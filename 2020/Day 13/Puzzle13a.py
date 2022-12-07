"""
Puzzle #13a - AdventOfCode
Read in bus scedule
determine which bus will have you waiting the shortest time
multiply that bus id by how long you'll have to wait
"""

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Schedule = []

    for Entry in File:
        Schedule.append(Entry.strip())
            
    return Schedule

def DetermineBus(Schedule):
    ArrivalTime = int(Schedule[0])
    ActiveBuses = [int(ActiveBus) for ActiveBus in Schedule[1].split(",") if ActiveBus != "x"]
    ActiveBuses.sort()
    BestBus = []
    EarliestTime = ActiveBuses[0] - (ArrivalTime % ActiveBuses[0])
    for Bus in ActiveBuses:
        
        RemainingMinutes = Bus - (ArrivalTime % Bus)
        
        if RemainingMinutes <= EarliestTime:
            if not BestBus:
                BestBus.append(Bus)
                BestBus.append(RemainingMinutes)
            else:
                BestBus[0] = Bus
                BestBus[1] = RemainingMinutes
    return BestBus

def main():
    Schedule = ReadInFile()
    BestBus = DetermineBus(Schedule)
    Answer = BestBus[0] * BestBus[1]

    print("Part 1: ", Answer)

if __name__ == "__main__":
    main()
