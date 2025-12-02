from collections import defaultdict, deque
import networkx as nx

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
        return content

def PartASolve(inputs):
    network = defaultdict(list)

    connections = inputs.split("\n")
    for connection in connections:
        key,value = connection.split("-")
        if value not in network[key]:
            network[key].append(value)
        if key not in network[value]:
            network[value].append(key)

    trinet = set()
    for k in network:
        for i in range(len(network[k])):
            c1 = network[k][i]
            for j in range(i+1,len(network[k])):
                c2 = network[k][j]
                if c2 in network[c1]:
                    mylist =[k,c1,c2]
                    mylist.sort()
                    trinet.add(tuple(mylist))
            
    trinet = list(trinet)
    total = 0

    for n1,n2,n3 in trinet:
        if n1.startswith("t") or n2.startswith("t") or n3.startswith("t"):
            total +=1

    return total            

def PartBSolve(inputs):
    network = defaultdict(list)

    connections = inputs.split("\n")
    for connection in connections:
        key,value = connection.split("-")
        if value not in network[key]:
            network[key].append(value)
        if key not in network[value]:
            network[value].append(key)

    G = nx.Graph()
    
    for k in network:
        G.add_node(k)
        for v in network[k]:
            G.add_edge(k,v)

    cliques = list(nx.find_cliques(G))
    result = max(cliques, key=len)
    result.sort()
    return ",".join(result)
    
                
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
