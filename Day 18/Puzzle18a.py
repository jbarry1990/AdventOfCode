"""
Puzzle #18a - AdventOfCode
1. Read problems line by line into an array
2. Solve each problem in the array using the following rules and store the answers to each problem in an array:
    1. Order of operations are Parentheses then left to right
3. Sum the answers and output the result
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Problems = []


    for Entry in File:
        Problems.append(Entry.strip())

    return Problems

def SimplifyProblems(Problems):
    Answers = []

    for Problem in Problems:
        Solved = False
        StringProblem = Problem
        while Solved == False:
            OpenParentheses = []
            ClosedParentheses = []
            for Index, Character in enumerate(StringProblem):
                if Character == "(":
                    OpenParentheses.append(Index)
                elif Character == ")":
                    ClosedParentheses.append(Index)

            if len(OpenParentheses) == 0 and len(ClosedParentheses) == 0:
                #solve addition multiplication from left to right
                Answers.append(SolveProblem(StringProblem))
                Solved = True

            else: #solve inner parenentheses and repeat
                StartOfProblem = int(OpenParentheses[-1])+1
                ClosedParen = -1
                for Parentheses in ClosedParentheses:
                    if Parentheses > OpenParentheses[-1]:
                        ClosedParen = int(Parentheses)
                        break
                EndOfProblem = ClosedParen
                SubAnswer = SolveProblem(StringProblem[StartOfProblem:EndOfProblem])
                StringProblem = StringProblem.replace(StringProblem[StartOfProblem -1:EndOfProblem + 1], str(SubAnswer))
                
                                         
                    
    return Answers

def SolveProblem(Problem):
    ProblemList = Problem.split(" ")
    while len(ProblemList) > 1:
        FirstNumber = int(ProblemList[0])
        SecondNumber = int(ProblemList[2])

        if ProblemList[1] == "+":
            ProblemList[0] = FirstNumber + SecondNumber
        elif ProblemList[1] == "*":
            ProblemList[0] = FirstNumber * SecondNumber

        ProblemList.remove(ProblemList[2])
        ProblemList.remove(ProblemList[1]) 
        
    Answer = ProblemList[0]

    return Answer

def SumAnswers(Answers):
    return sum(Answers)

def main():
    t_start = time()

    Problems = ReadInFile()
    Answers = SimplifyProblems(Problems)
    Answer = SumAnswers(Answers)

    print("Part 1: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
