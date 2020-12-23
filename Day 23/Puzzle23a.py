"""
Puzzle #22a - AdventOfCode
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    CupOrder = []

    for Line in File:
        for Character in Line.strip():
            CupOrder.append(int(Character))

    return CupOrder

def PlayGame(NumberOfRounds, CupOrder):

    RoundCount = 1
    CurrentCup = CupOrder[0]
    LastIndex = len(CupOrder)-1
    TargetCup = 0

    while RoundCount <=NumberOfRounds:
        IndexOfCurrentCup = CupOrder.index(CurrentCup)
        CupsToPull = []
        if IndexOfCurrentCup + 3 > LastIndex:
            NumberOfWrappedElements = 3-(LastIndex - IndexOfCurrentCup)
            if NumberOfWrappedElements == 3:
                CupsToPull = [CupOrder.pop(Number) for Number in range(2,-1,-1)]
                CupsToPull.reverse()
            elif NumberOfWrappedElements == 2:
                CupsToPull.append(CupOrder.pop(1))
                CupsToPull.append(CupOrder.pop(0))
                CupsToPull.append(CupOrder.pop(-1))
                CupsToPull.reverse()
                
            elif NumberOfWrappedElements == 1:
                CupsToPull.append(CupOrder.pop(-2))
                CupsToPull.append(CupOrder.pop(-1))
                CupsToPull.append(CupOrder.pop(0))
        else:
            CupsToPull = [CupOrder.pop(Number) for Number in range(IndexOfCurrentCup+3,IndexOfCurrentCup,-1)]
            CupsToPull.reverse()
            
        if CurrentCup > 1:
            TargetCup = CurrentCup-1
        else:
            TargetCup = max(CupOrder)
            
        while TargetCup in CupsToPull:
            if TargetCup > 1:
                TargetCup -= 1
            else:
                TargetCup = max(CupOrder)

        TargetCupIndex = CupOrder.index(TargetCup)
        CupOrder.insert(TargetCupIndex+1,CupsToPull[2])
        CupOrder.insert(TargetCupIndex+1,CupsToPull[1])
        CupOrder.insert(TargetCupIndex+1,CupsToPull[0])
        
        IndexOfCurrentCup = CupOrder.index(CurrentCup)
        if IndexOfCurrentCup == LastIndex:
            CurrentCup = CupOrder[0]
        else:
            CurrentCup=CupOrder[IndexOfCurrentCup+1]
        RoundCount += 1
       
    return CupOrder

def FormatAnswer(FinalOrder):
    Answer="".join([str(Number) for Number in FinalOrder])
    SubAnswer = Answer.split("1")
    Answer = SubAnswer[1]+SubAnswer[0]

    return Answer

def main():
    t_start = time()

    CupOrder = ReadInFile()
    FinalOrder = PlayGame(100, CupOrder)
    Answer = FormatAnswer(FinalOrder)

    print("Part 1: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
