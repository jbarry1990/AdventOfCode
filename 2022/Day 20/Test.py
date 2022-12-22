from collections import deque

def ReadInputs():
        File = open("./Inputs.txt", "r")
        Numbers = []
        for Line in File:
            Numbers.append(int(Line.strip()))

        return Numbers
    
def solveA(lines, part):
    X = [int(x) for x in lines]
    if part == 2:
        X = [x*811589153 for x in X]
    X = deque(list(enumerate(X)))
    for t in range(10 if part==2 else 1):
        for i in range(len(X)):
            for j in range(len(X)):
                if X[j][0]==i:
                    break
            while X[0][0]!=i:
                X.append(X.popleft())
            val = X.popleft()
            to_pop = val[1]
            to_pop %= len(X)
            assert 0<=to_pop < len(X)

            for _ in range(to_pop):
                X.append(X.popleft())
            X.append(val)

    ZeroIndex = -1
    for j in range(len(X)):
        if X[j][1] == 0:
            ZeroIndex = j
            break
    print(X[(ZeroIndex+1000)%len(X)][1])
    print(X[(ZeroIndex+2000)%len(X)][1])
    print(X[(ZeroIndex+3000)%len(X)][1])
    return (X[(ZeroIndex+1000)%len(X)][1] + X[(ZeroIndex+2000)%len(X)][1] + X[(ZeroIndex+3000)%len(X)][1])
    print(solve(1))
    print(solve(2))

    


    return

def solveB(Input):
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input,1)
    print("Answer: ", Part1)
    Part2=solveA(Input,2)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
