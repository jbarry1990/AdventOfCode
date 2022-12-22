from collections import deque
def ReadInputs():
        File = open("./Inputs.txt", "r")
        Data = File.read().strip()
        Lines = [Line for Line in Data.split("\n")]

        return Lines

def CollectGeode(OreBotCost, ClayBotCost, ObsidianBotCost, GeodeBotCost, StartTime, Resources, BotCounts):
    best = 0
    MaxOreCost = max(OreBotCost[0], ClayBotCost[0], ObsidianBotCost[0], GeodeBotCost[0])
    MaxClayCost = ObsidianBotCost[1]
    MaxObsidianCost = GeodeBotCost[1]
    MaxOreCost = max(OreBotCost[0], ClayBotCost[0], ObsidianBotCost[0], GeodeBotCost[0])
    State = (0,0,0,0,1,0,0,0, StartTime)
    Queue = deque([State])
    print(Queue)
    Seen = set()
    #for _ in range(3):
    while Queue:
        State = Queue.popleft()

        OreCount, ClayCount, ObsidianCount, GeodeCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time = State

        #print(GeodeCount, ": ", best)
        best = max(best, GeodeCount)
        if Time == 0:
            continue
        if OreBotCount >= MaxOreCost:
            OreBotCount = MaxOreCost
        if ClayBotCount >= MaxClayCost:
            ClayBotCount = MaxClayCost
        if ObsidianBotCount >= MaxObsidianCost:
            ObsidianBotCount = MaxObsidianCost
        if OreCount >= Time*MaxOreCost-OreBotCount*(Time-1):
            OreCount = Time*MaxOreCost-OreBotCount*(Time-1)
        if ClayCount>=Time*ClayBotCost[1]-ClayBotCount*(Time-1):
            ClayCount = Time*ClayBotCost[1]-ClayBotCount*(Time-1)
        if ObsidianCount>=Time*GeodeBotCost[1]-ObsidianBotCount*(Time-1):
            ObsidianCount = Time*GeodeBotCost[1]-ObsidianBotCount*(Time-1)

        state = (OreCount,ClayCount,ObsidianCount,GeodeCount,OreBotCount,ClayBotCount,ObsidianBotCount,GeodeBotCount,Time)
        if State in Seen:
            continue
        Seen.add(State)

        # Collect resources
        if len(Seen) % 1000000 == 0:
            print(best,",",len(Seen))
        Queue.append((OreCount+OreBotCount, ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time-1))
        if OreCount >= OreBotCost[0] and OreBotCount:
            print("I'm buying an OreBot")
            Queue.append((OreCount+OreBotCount-OreBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount+1, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time-1))
        if OreCount >= ClayBotCost[0] and ClayBotCount:
            print("I'm buying a ClayBot")
            Queue.append((OreCount+OreBotCount-ClayBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount+1, ObsidianBotCount, GeodeBotCount, Time-1))
        if OreCount >= ObsidianBotCost[0] and ClayCount >= ObsidianBotCost[1] and ObsidianBotCount:
            Queue.append((OreCount+OreBotCount-ObsidianBotCost[0], ClayCount+ClayBotCount-ObsidianBotCost[1], ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount+1, GeodeBotCount, Time-1))
        if OreCount >= GeodeBotCost[0] and ObsidianCount >= GeodeBotCost[1]:
            print("We have a geodebot")
            Queue.append((OreCount+OreBotCount-GeodeBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount-GeodeBotCost[1], GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount+1, Time-1))

    return best

def solveA(Blueprints):
    Answer = 0
    for Blueprint in Blueprints:
        Words = Blueprint.split()
        BlueprintID = int(Words[1][:-1])
        OreBotCost = [int(Words[6]), 0] 
        ClayBotCost = [int(Words[12]), 0]
        ObsidianBotCost = [int(Words[18]), int(Words[21])]
        GeodeBotCost = [int(Words[27]), int(Words[30])]
        Answer = CollectGeode(OreBotCost, ClayBotCost, ObsidianBotCost, GeodeBotCost, 24, [0, 0, 0, 0], [1,0,0,0])
        Answer += (Answer*BlueprintID)
    return Answer

def solveB(Input):
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
