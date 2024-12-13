def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    polymers = {}
    
    pairs = {}
    count = {}
    polymer = [x for x in file_contents[0].strip("\n")]

    for index, element in enumerate(polymer):
        if index == len(polymer)-1:
            break
        if (element + polymer[index+1]) in polymers:
            polymers[element + polymer[index+1]] +=1
        else:
            polymers[element + polymer[index+1]] =1
            
    for line in file_contents[2:]:
        key, value = line.strip().split(" -> ")
        pairs[key] = value
        count[value] = 0

    for character in polymer:
        count[character]+=1

    return polymers, pairs, count

def PairInsertion(polymer, pairs, count):

    new_polymer = {}

    for (a,b), value in polymer.items():
        insert = pairs[a+b]

        if a+insert in new_polymer:
            new_polymer[a+insert] +=value
        else:
            new_polymer[a+insert] = value

        if insert+b in new_polymer:
            new_polymer[insert+b] +=value
        else:
            new_polymer[insert+b] = value

        count[insert] +=value
        
    return new_polymer, count

def Delta(count):
    highest = max(count.values())
    lowest = min(count.values())

    answer = highest - lowest
            
    return answer

def PartASolve(polymer, pairs, count, steps):
    for step in range(steps):
        polymer, count = PairInsertion(polymer, pairs, count)

    answer = Delta(count)
        
    return answer
            
def PartBSolve(polymer, pairs, count, steps):
    for step in range(steps):
        polymer, count = PairInsertion(polymer, pairs, count)

    answer = Delta(count)

    return answer

def main():
    file_contents = ReadFile("Inputs.txt")
    polymer, pairs, count = ParseFile(file_contents)
    answer = PartASolve(polymer, pairs, count, 10)
    print("Part A Answer: ", answer)

    polymer, pairs, count = ParseFile(file_contents)
    answer = PartBSolve(polymer, pairs, count, 40)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
