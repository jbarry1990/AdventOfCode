import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read()
        content = content.split("\n\n")
        stripped_content = [x.split("\n") for x in content]
        return stripped_content

def SolveVertical(block):
    return (False,-1)

def SolveA(block):
    for i in range(1,len(block)):
        chunk = block[max(0,i-(len(block)-i)):min(2*i,len(block))]
        for j,row in enumerate(chunk):
            if row == chunk[len(chunk)-(j+1)]:
                continue
            else:
                break
        else:
            return True,i
                
    return False,-1

def PartASolve(file_contents):
    vert = []
    horz = []
    for block in file_contents:
        h,index = SolveA(block)
        if h == True:
            horz.append(index)
            continue
        else:
            block_list = [list(x) for x in block]
            transpose = [[row[i] for row in block_list] for i in range(len(block_list[0]))]
            transpose = ["".join(x) for x in transpose]
            v,index = SolveA(transpose)
            if v == True:
                vert.append(index)
                continue

    total = 0
    total +=sum(vert)
    total +=sum(horz)*100
            
    return total

def SolveB(block):
##    print("Block:")
##    for x in block:
##        print(x)
##    print()
    for i in range(1,len(block)):
        chunk = block[max(0,i-(len(block)-i)):min(2*i,len(block))]
##        print(i)
##        print("Chunk:")
##        for x in chunk:
##            print(x)
##        print()
        for r,line in enumerate(chunk):
            for c,ch in enumerate(line):
                chunk_list = chunk.copy()
                chunk_list = [list(x) for x in chunk_list]
                if ch == "#":
                    chunk_list[r][c] = "."
                else:
                    chunk_list[r][c] = "#"
                new_chunk = ["".join(x) for x in chunk_list]
##                print("New Chunk:")
##                for x in new_chunk:
##                    print(x)
##                print()
                
                for j,row in enumerate(new_chunk):
                    if row == new_chunk[len(new_chunk)-(j+1)]:
                        continue
                    else:
                        break
                else:
                    return True,i
                        
    return False,-1   

def PartBSolve(file_contents):        
    vert = []
    horz = []
    for block in file_contents:
        h,index = SolveB(block)
        if h == True:
            horz.append(index)
            continue
        else:
            block_list = [list(x) for x in block]
            transpose = [[row[i] for row in block_list] for i in range(len(block_list[0]))]
            transpose = ["".join(x) for x in transpose]
            v,index = SolveB(transpose)
            if v == True:
                vert.append(index)
                continue

    total = 0
    total +=sum(vert)
    total +=sum(horz)*100

    return total

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
