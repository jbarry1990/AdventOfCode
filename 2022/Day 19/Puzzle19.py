def ReadInputs():
        File = open("./Inputs.txt", "r")
        Data = File.read().strip()
        Lines = [Line for Line in Data.split("\n")]

        return Lines

def CollectGeode(OreBotCost, ClayBotCost, ObsidianBotCost, GeodeBotCost, StartTime, Resources, BotCounts):
    best = 0
    Queue = []
    State = (Resources[0],Resources[1], Resources[2], Resources[3], BotCounts[0], BotCounts[1], BotCounts[2], BotCounts[3], StartTime)
    Queue.append(State)
    print(Queue)
    Seen = set()
    while Queue != []:
        State = Queue.pop()

        if State in Seen:
            continue
        Seen.add(State)

        OreCount, ClayCount, ObsidianCount, GeodeCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time = State

        best = max(best, GeodeCount)
        if Time == 0:
            continue
        
        # Collect resources
        Queue.insert(0,(OreCount+OreBotCount, ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time-1))
        if OreCount >= OreBotCost[0]:
            Queue.insert(0,(OreCount+OreBotCount-OreBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount+1, ClayBotCount, ObsidianBotCount, GeodeBotCount, Time-1))
        if ClayCount >= ClayBotCost[0]:
            Queue.insert(0,(OreCount+OreBotCount-ClayBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount+1, ObsidianBotCount, GeodeBotCount, Time-1))
        if OreCount >= ObsidianBotCost[0] and ClayCount >= ObsidianBotCost[1]:
            Queue.insert(0,(OreCount+OreBotCount-ObsidianBotCost[0], ClayCount+ClayBotCount-ObsidianBotCost[1], ObsidianCount+ObsidianBotCount, GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount+1, GeodeBotCount, Time-1))
        if OreCount >= GeodeBotCost[0] and ObsidianCount >= GeodeBotCost[1]:
            Queue.insert(0,(OreCount+OreBotCount-GeodeBotCost[0], ClayCount+ClayBotCount, ObsidianCount+ObsidianBotCount-GeodeBotCost[1], GeodeCount+GeodeBotCount, OreBotCount, ClayBotCount, ObsidianBotCount, GeodeBotCount+1, Time-1))
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
