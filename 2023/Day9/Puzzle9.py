import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content

def SolveSequenceA(seq):
    if len(set(seq)) == 1:
        return seq
    nseq = [seq[i]-seq[i-1] for i in range(1,len(seq))]
    nseq = SolveSequenceA(nseq)
    seq.append(nseq[-1]+seq[-1])
    return seq

def SolveSequenceB(seq):
    if len(set(seq)) == 1:
        return seq
    nseq = [seq[i]-seq[i-1] for i in range(1,len(seq))]
    nseq = SolveSequenceB(nseq)
    seq.insert(0,seq[0]-nseq[0])
    return seq

def PartASolve(file_contents):
    sequences = [[int(i) for i in line.split()] for line in file_contents]

    predictions = []
    for seq in sequences:
        predictions.append(SolveSequenceA(seq)[-1])
    return sum(predictions)
            
def PartBSolve(file_contents):        
    sequences = [[int(i) for i in line.split()] for line in file_contents]

    predictions = []
    for seq in sequences:
        predictions.append(SolveSequenceB(seq)[0])
    return sum(predictions)

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
