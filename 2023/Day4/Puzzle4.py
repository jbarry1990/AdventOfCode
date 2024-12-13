import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
def InRange(coord, h, w):
    if coord[0] <= h-1 and coord[0] >= 0 and coord[1] <= w-2 and coord[1] >=0:
        return True
    return False

def PartASolve(file_contents):
    points_per_round = []
    for line in file_contents:
        winning_numbers, numbers = line.split("|")
        numbers=numbers.strip()
        numbers = [int(n) for n in numbers.split()]
        winning_numbers = winning_numbers.split(":")[1].strip()
        winning_numbers = [int(n) for n in winning_numbers.split()]

        points = 0
        for n in winning_numbers:
            if n in numbers:
                points +=1
        if points > 0:
            points_per_round.append(2**(points-1))
        else:
            points_per_round.append(0)
    return sum(points_per_round)                                                                     
                
def PartBSolve(file_contents):
    num_cards = 0
    boards = {i:1 for i in range(1,len(file_contents)+1)}
    for line in file_contents:
        winning_numbers, numbers = line.split("|")
        numbers=numbers.strip()
        numbers = [int(n) for n in numbers.split()]
        game_id, winning_numbers = winning_numbers.split(":")
        winning_numbers = winning_numbers.strip()
        game_id = int(game_id.split()[1])
        winning_numbers = [int(n) for n in winning_numbers.split()]

        points = 0
        for n in winning_numbers:
            if n in numbers:
                points +=1
        for i in range(points):
            boards[game_id+1+i] += boards[game_id]

    for k,v in boards.items():
        num_cards +=v

    return num_cards

        

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
