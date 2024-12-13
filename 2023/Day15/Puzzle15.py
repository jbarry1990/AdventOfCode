import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content

def Hash(seq):
    current = 0
    for ch in seq:
        current += ord(ch)
        current *= 17
        current %= 256
    return current

def PartASolve(file_contents):
    seq = file_contents[0].split(",")

    total = 0
    for s in seq:
        total += Hash(s)
    
    return total

def PartBSolve(file_contents):
    seq = file_contents[0].split(",")
    boxes = [[] for i in range(256)]

    for s in seq:
        if "=" in s:
            box_ch,lens_num = s.split("=")
            lens_num = int(lens_num)
            box_num = Hash(box_ch)
            for ch,lens in boxes[box_num]:
                if box_ch == ch:
                    index = boxes[box_num].index([ch,lens])
                    boxes[box_num][index][1] = lens_num
                    break
            else:
                boxes[box_num].append([box_ch,lens_num])
                
        else:
            box_ch = s[:-1]
            box_num = Hash(box_ch)
            for ch,lens in boxes[box_num]:
                if box_ch == ch:
                    index = boxes[box_num].index([ch,lens])
                    boxes[box_num].pop(index)
                    break
    total = 0
    for i,box in enumerate(boxes):
        if box != []:
            for j,el in enumerate(box):
                ch,l = el
                total += (i+1)*(j+1)*l

    return total

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
