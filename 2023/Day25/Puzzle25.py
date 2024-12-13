import networkx as nx

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    g = nx.Graph()

    for line in file_contents:
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    print(len(a) * len(b))
        
    return


def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)

if __name__ == "__main__":
    main()
