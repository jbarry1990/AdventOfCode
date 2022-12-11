def ReadInputs():
        File = open("./Inputs.txt", "r")

        return File.read().strip()
    
def solveA(Code):
    Answer = -1
    for Index, Character in enumerate(Code):
        if(Index+1 >=len(Code) or (Index+2 >=len(Code) or Index+3 >=len(Code))):
            break
        if Character == Code[Index+1] or Character == Code[Index+2] or Character == Code[Index+3]:
            continue
        elif Code[Index+1] == Code[Index+2] or Code[Index+1] == Code[Index+3]:
            continue
        elif Code[Index+2] == Code[Index+3]:
            continue
        else:
            Answer = Index+4
            break

    return Answer

def solveB(Code):
    Answer = -1
    for Index, Character in enumerate(Code):
        Snippet = Code[Index:Index+14]
        SnippetSet = set(Snippet)
        if(len(Snippet) == len(SnippetSet)):
            print(Index)
            Answer = Index+14
            break
    return Answer

def main():

    Code=ReadInputs()
    Part1=solveA(Code)
    print("Answer: ", Part1)
    Part2=solveB(Code)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
