def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    code = []
    for line in file_contents:
        code.append(line.strip("\n"))

    return code
        
def PartASolve(code):
    open_brackets = [ "(", "[", "{", "<"]
    closed_brackets = [ ")", "]", "}", ">"]
    expected_symbol = []
    corrupted = []
    corrupted_lines = []
    points = dict({")":3, "]":57, "}":1197, ">":25137})

    for line_index, line in enumerate(code):
        for chunk in line:
            if chunk in open_brackets:
                index = open_brackets.index(chunk)
                expected_symbol.insert(0, closed_brackets[index])
            else:
                if expected_symbol[0] == chunk:
                    expected_symbol.pop(0)
                else:
                    corrupted.append(chunk)
                    corrupted_lines.insert(0, line_index)
                    break
    score = 0
    for character in corrupted:
        score += points[character] 
    return score, corrupted_lines

def PartBSolve(code, corrupted_lines):
    open_brackets = [ "(", "[", "{", "<"]
    closed_brackets = [ ")", "]", "}", ">"]
    line_endings = []
    scores = []

    points = dict({")":1, "]":2, "}":3, ">":4})

    #remove corrupted lines
    for line in corrupted_lines:
        code.pop(line)

    for line_index, line in enumerate(code):
        expected_symbol = []
        for chunk in line:
            if chunk in open_brackets:
                index = open_brackets.index(chunk)
                expected_symbol.insert(0, closed_brackets[index])
            else:
                if expected_symbol[0] == chunk:
                    expected_symbol.pop(0)
                    
        line_endings.append(expected_symbol)

    for line in line_endings:
        score = 0
        for character in line:
            score = (score * 5) + points[character]
        scores.append(score)

    scores.sort()
    index = len(scores)//2
    return scores[index]

def main():
    file_contents = ReadFile("Inputs.txt")
    code = ParseFile(file_contents)
    answer, corrupted_lines = PartASolve(code)
    print("Part A Answer: ", answer)
    answer = PartBSolve(code, corrupted_lines)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
