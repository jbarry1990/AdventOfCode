def ReadInputs():
    File = open("./Inputs.txt", "r")
    Matches = []
    
    for Line in File:
    	Matches.append(Line.strip())
 
    return Matches
    
def solveA(Matches):
# Win = 6
# Draw = 3
# Loss = 0
# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3
    scores = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9, "C X":7, "C Y":2, "C Z":6}
    
    score = 0
    for Match in Matches:
        score += scores[Match]
            
    return score
    
def solveB(Matches):
# Win = 6
# Draw = 3
# Loss = 0
# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
# X = Lose
# Y = Draw
# Z = Win
    scores = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7}
    
    score = 0
    for Match in Matches:
        score += scores[Match]
            
    return score
    
def main():

    Inputs=ReadInputs()
    Part1=solveA(Inputs)
    print("Answer: ", Part1)
    Part2=solveB(Inputs)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
