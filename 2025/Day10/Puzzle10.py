import shapely
def ReadInputs():
    File = open("./Inputs.txt", "r")
    Lines = File.readlines()
    machines = {i:{"lights" : [], "buttons":[], "power":[]} for i in range(len(Lines))}

    for i,line in enumerate(Lines):
        items = line.strip().split(" ")
        for item in items:
            if item.startswith("["):
                machines[i]["lights"] = list(item[1:-1])
            elif item.startswith("("):
                if "," in item:
                    machines[i]["buttons"].append([int(x) for x in item[1:-1].split(",")])
                else:
                    machines[i]["buttons"].append([int(item[1:-1])])
            elif item.startswith("{"):
                machines[i]["power"] = [int(x) for x in item[1:-1].split(",")]

    return machines

def solveA(Input):
    return
                
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
