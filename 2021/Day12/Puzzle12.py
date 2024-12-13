def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    # parse inputs into a list of connections
    #iterate through the list and add
    tunnels = []
    connections ={}

    for line in file_contents:
        tunnels.append(line.strip("\n").split("-"))

    for tunnel in tunnels:
        if "start" in tunnel:
            if tunnel[0] == "start":
                if tunnel[0] not in connections:
                    connections[tunnel[0]] = [tunnel[1]]
                else:
                    connections[tunnel[0]].append(tunnel[1])
            else:
                if tunnel[1] not in connections:
                    connections[tunnel[1]] = [tunnel[0]]
                else:
                    connections[tunnel[1]].append(tunnel[0])
            continue
        
        else:
            if tunnel[0] not in connections:
                connections[tunnel[0]] = [tunnel[1]]
            else:
                connections[tunnel[0]].append(tunnel[1])

            if tunnel[1] not in connections:
                connections[tunnel[1]] = [tunnel[0]]
            else:
                connections[tunnel[1]].append(tunnel[0])
    
    return connections

def FindRoute(start, visited, connections, path_count):
    
    if start == "end":
        path_count[0] +=1
        visited.remove(start)
        return

    for connection in connections[start]:
        # checks to make sure I don't go back to a small cave
        if connection.islower() and connection in visited:
            continue

        if connection.islower():
            visited.append(connection)
            
        FindRoute(connection, visited, connections, path_count)
        if connection in visited:
            visited.remove(connection)
        
def PartASolve(connections):
    path_count = [0]
    FindRoute("start", list(), connections, path_count)
    return path_count[0]

def FindRouteB(start, visited, connections, path_count):
    if start.islower():
        visited[start] +=1
    
    if start == "end":
        path_count[0] +=1
        visited[start] = 0
        return

    #loop through the possible connections
    for connection in connections[start]:

        # if we've visited the cave once already check that another cave
        # wasn't already visited twice. If it was then we skip this path as it's
        # invalid. Otherwise the path is valid and we should follow it.
        if connection.islower() and visited[connection] > 0:
            if 2 in visited.values():
                continue
            
        FindRouteB(connection, visited, connections, path_count)
        visited[connection] -= 1 
            
def PartBSolve(connections):
    path_count = [0]
    visited = {}
    for connection in connections:
        visited[connection] = 0

    FindRouteB("start", visited, connections, path_count)
    return path_count[0]

def main():
    file_contents = ReadFile("Inputs.txt")
    connections = ParseFile(file_contents)
    answer = PartASolve(connections)
    print("Part A Answer: ", answer)
    answer = PartBSolve(connections)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
