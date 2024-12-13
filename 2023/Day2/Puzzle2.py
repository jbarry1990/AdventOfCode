def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(file_contents):
    colors = ["red", "blue", "green"]
    num_cubes = [12, 14, 13]
    possible_games = set()
    impossible_games = set()
    for line in file_contents:
        is_valid = True
        game_id,games = line.split(":")
        games = [x.strip() for x in games.split(";")]
        for game in games:
            results = [x.strip() for x in game.split(",")]
            for result in results:
                for i, color in enumerate(colors):
                    if result.find(color) != -1:
                        if int(result[0:2]) > num_cubes[i]:
                            impossible_games.add(int(game_id.split()[1]))
                            is_valid = False
                            break
            if is_valid == False:
                break
            
        if is_valid:
            possible_games.add(int(game_id.split()[1]))
            
    return sum(possible_games)

def PartBSolve(file_contents):
    colors = ["red", "blue", "green"]
    num_cubes = [12, 14, 13]
    powers =[]
    for line in file_contents:
        min_cubes = [0,0,0]
        game_id,games = line.split(":")
        games = [x.strip() for x in games.split(";")]
        for game in games:
            results = [x.strip() for x in game.split(",")]
            for result in results:
                for i, color in enumerate(colors):
                    if result.find(color) != -1:
                        if min_cubes[i] < int(result[0:2]):
                            min_cubes[i] = int(result[0:2])
        result = 1
        for cube in min_cubes:
            result *= cube
        powers.append(result)
                        
            
    return sum(powers)
def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
