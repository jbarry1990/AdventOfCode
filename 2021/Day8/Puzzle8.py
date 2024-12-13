def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    codes = []
    for index, line in enumerate(file_contents):
        #sort all patterns by length of strings to make sure 1,4,7,8 are in order and sort the characters for uniformity as the letters order don't matter
        pattern = sorted(["".join(sorted(digit)) for digit in line.strip("\n").split(" | ")[0].split()], key=len)
        #sort all output strings characters for uniformity since letter order doesn't matter
        output = ["".join(sorted(digit)) for digit in line.strip("\n").split(" | ")[1].split()]
        codes.append([pattern, output])
    return codes

def PartASolve(codes):
    count = 0
    for code in codes:
        for output in code[1]:
            length = len(output)
            if length < 5 or length > 6:
                count += 1
    return count

def CommonSubString(a, b):
    count = 0
    for character in a:
        if character in b:
            count +=1
    return count

def SolveOutputString(digit_map, output_list):
    numbers=[]
    
    for output in output_list:
        for digit in digit_map:
            if digit_map[digit] == output:
                numbers.append(digit)
                break
    number = 0
    number += numbers[0]*1000
    number += numbers[1]*100
    number += numbers[2]*10
    number += numbers[3]

    return number

def PartBSolve(codes):
    output_as_digits = []
    
    for display in codes:
        pattern = display[0]
        output = display[1]
        
        #1, 4, 7, 8
        digit_map = dict({1:pattern[0], 7:pattern[1], 4:pattern[2], 8:pattern[9]})
        #2,3,5 have 5 segments in them
        five_segment_digits = [pattern[3], pattern[4], pattern[5]]
        #0, 6, 9 have 6 segments in them 
        six_segment_digits = [pattern[6], pattern[7], pattern[8]]

        #find 9
        for digit in six_segment_digits:
            if CommonSubString(digit_map[4], digit) == 4:
                digit_map[9] = digit
                six_segment_digits.remove(digit)
                break

        #find 0
        for digit in six_segment_digits:
            if CommonSubString(digit_map[7], digit) == 3:
                digit_map[0] = digit
                six_segment_digits.remove(digit)
                break
            
        #find 6
        digit_map[6] = six_segment_digits[0]
                
        #find 3
        for digit in five_segment_digits:
            if CommonSubString(digit_map[1], digit) == 2:
                digit_map[3] = digit
                five_segment_digits.remove(digit)
                break
        #find 5
        for digit in five_segment_digits:
            if CommonSubString(digit_map[4], digit) == 3:
                digit_map[5] = digit
                five_segment_digits.remove(digit)
                break
        #find 2
        digit_map[2] = five_segment_digits[0]

        output_as_digits.append(SolveOutputString(digit_map, output))

    sum = 0
    for digit in output_as_digits:
        sum += digit
        
    return sum

def main():
    file_contents = ReadFile("Inputs.txt")
    codes = ParseFile(file_contents)
    answer = PartASolve(codes)
    print("Part A Answer: ", answer)
    answer = PartBSolve(codes)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
