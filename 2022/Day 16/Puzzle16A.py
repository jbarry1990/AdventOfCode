# Part 1 works but Part 2 doesn't for some reason
def ReadInputs():
    File = open("./Inputs.txt", "r")
    Data = File.read().strip()
    Lines = [Line for Line in Data.split("\n")]

    Rates = {}
    ConnectedTunnels = {}
    for Line in Lines:
        Words = Line.split()
        ID = Words[1]
        Rate = int(Words[4][5:-1])
        Tunnels = [x for x in "".join(Words[9:]).split(",")]
        for Tunnel in Tunnels:
            if ID in ConnectedTunnels:
                ConnectedTunnels[ID].append(Tunnel)
            else:
                ConnectedTunnels[ID] = [Tunnel]
        Rates[ID] = Rate

    return Rates, ConnectedTunnels

DP = {}

def FindScore(CurrentPosition, Visited, Time, Rates, ConnectedTunnels, NumberOfPlayers):
    if Time == 0:
        if NumberOfPlayers > 1:
            Answer = FindScore("AA",Visited, 26, Rates, ConnectedTunnels, 1)
            return Answer
        else:
            return 0

    Key = (CurrentPosition,tuple(sorted(Visited)),Time)
    if Key in DP:
        return DP[Key]

    Answer = 0
    if Time > 0 and CurrentPosition not in Visited and Rates[CurrentPosition] > 0:
        NewVisited = set(Visited)
        NewVisited.add(CurrentPosition)
        Answer = max(Answer, sum(Rates[Open] for Open in Visited) + FindScore(CurrentPosition, NewVisited, Time-1,Rates, ConnectedTunnels, NumberOfPlayers))

    if Time > 0:
        for Tunnel in ConnectedTunnels[CurrentPosition]:
            Answer = max(Answer, sum(Rates[Open] for Open in Visited) + FindScore(Tunnel, Visited,Time-1,Rates,ConnectedTunnels,NumberOfPlayers))
    
    DP[Key] = Answer

    return Answer

def solveA(Rates, ConnectedTunnels):
    Answer = FindScore("AA", set(), 30, Rates, ConnectedTunnels, 1)
    return Answer

def solveB(Rates, ConnectedTunnels):
    Answer = FindScore("AA", set(), 26, Rates, ConnectedTunnels, 2)
    return Answer

def main():

    Rates, ConnectedTunnels=ReadInputs()
    #Part1=solveA(Rates, ConnectedTunnels)
    #print("Answer: ", Part1)
    Part2=solveB(Rates, ConnectedTunnels)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
