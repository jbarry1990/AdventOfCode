import math

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    cycles = 1000
    paths = dict()
    states = dict()
    conjunctions = dict()

    for line in file_contents:
        module,nodes = line.split("->")
        if module.startswith("%"):
            paths[module[1:-1]] = nodes.replace(" ","").split(",")
            states[module[1:-1]] = (module[0],0,0)
        elif module.startswith("&"):
            paths[module[1:-1]] = nodes.replace(" ","").split(",")
            states[module[1:-1]] = (module[0],0,0)
            conjunctions[module[1:-1]] = []
        else:
            paths[module[:-1]] = nodes.replace(" ","").split(",")

    for k,v in conjunctions.items():
        for mods,path in paths.items():
            if k in path:
                conjunctions[k].append(mods)



    high = 0
    low = 0
    for i in range(cycles):
        Queue = [("broadcaster",0)]
        while Queue:
            module,signal = Queue.pop(0)
                
            if module not in paths:
                continue

            if module != "broadcaster":
                mod_type,status,last_sig = states[module]
                if mod_type == "%":
                    if signal == 0:
                        status = not status
                        if status:
                            last_sig = 1
                        else:
                            last_sig = 0
                        states[module] = (mod_type,status,last_sig)
                    else:
                        continue
                else:
                    for in_mod in conjunctions[module]:
                        if states[in_mod][2] == 0:
                            last_sig = 1
                            break
                    else:
                        last_sig = 0

                    states[module] = (mod_type,status,last_sig)
                        
                nodes = paths[module]
                for node in nodes:
                    Queue.append((node,states[module][2]))
                    if states[module][2] == 0:
                        low += 1
                    else:
                        high +=1

            else:
                low += 1
                nodes = paths[module]
                for node in nodes:
                    Queue.append((node, 0))
                    low +=1

    return high*low

def PartBSolve(file_contents):        
    paths = dict()
    states = dict()
    conjunctions = dict()

    for line in file_contents:
        module,nodes = line.split("->")
        if module.startswith("%"):
            paths[module[1:-1]] = nodes.replace(" ","").split(",")
            states[module[1:-1]] = (module[0],0,0)
        elif module.startswith("&"):
            paths[module[1:-1]] = nodes.replace(" ","").split(",")
            states[module[1:-1]] = (module[0],0,0)
            conjunctions[module[1:-1]] = []
        else:
            paths[module[:-1]] = nodes.replace(" ","").split(",")

    for k,v in conjunctions.items():
        for mods,path in paths.items():
            if k in path:
                conjunctions[k].append(mods)

    presses = 0

    (feed,) = [name for name,outputs in paths.items() if "rx" in outputs]
    cycle_lengths = {}
    seen = {name:0 for name,outputs in paths.items() if feed in outputs}

    while True:
        presses +=1
        Queue = [(None,"broadcaster",0)]
        while Queue:
            origin,module,signal = Queue.pop(0)
                
            if module not in paths:
                continue

            if module == feed and signal == 1:
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses

                if all(seen.values()):
                    x = 1
                    for cycles in cycle_lengths.values():
                        x = math.lcm(x,cycles)
                    return x
                    
                    
                
            if module != "broadcaster":
                mod_type,status,last_sig = states[module]
                if mod_type == "%":
                    if signal == 0:
                        status = not status
                        if status:
                            last_sig = 1
                        else:
                            last_sig = 0
                        states[module] = (mod_type,status,last_sig)
                    else:
                        continue
                else:
                    for in_mod in conjunctions[module]:
                        if states[in_mod][2] == 0:
                            last_sig = 1
                            break
                    else:
                        last_sig = 0

                    states[module] = (mod_type,status,last_sig)
                        
                nodes = paths[module]
                for node in nodes:
                    Queue.append((module,node,states[module][2]))

            else:
                nodes = paths[module]
                for node in nodes:
                    Queue.append((module,node, 0))


def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
