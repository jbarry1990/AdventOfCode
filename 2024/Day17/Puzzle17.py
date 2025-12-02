from collections import deque
import heapq

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
    return content
def Adjust(operand,A,B,C):
    if operand == 4:
        operand = A
    elif operand == 5:
        operand = B
    elif operand == 6:
        operand = C
    return operand

def PartASolve(inputs):
    registers,program = inputs.split("\n\n")
    registers = registers.split("\n")
    #A = int(registers[0].split()[2])
    A = 108107566389757
    B = int(registers[1].split()[2])
    C = int(registers[2].split()[2])

    program = program[9:].split(",")
    program = [int(x) for x in program]

    outputs = []
    pointer = 0
    while True:
        opcode = program[pointer]
        operand = program[pointer+1]

        if opcode == 0:
            operand = Adjust(operand,A,B,C)
            A = A//(2**operand)
        elif opcode == 1:
            B=B^operand
        elif opcode == 2:
            operand = Adjust(operand,A,B,C)
            B = operand%8
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:
            B = B^C
        elif opcode == 5:
            operand = Adjust(operand,A,B,C)
            outputs.append(operand%8)
        elif opcode == 6:
            operand = Adjust(operand)
            B = A//(2**operand)
        else:
            operand = Adjust(operand,A,B,C)
            C = A//(2**operand)
        if pointer == len(program)-2:
            break
        pointer += 2

    return ",".join(str(num) for num in outputs)
        
def Solve(program,ans):
    if program == []:
        return ans
    for t in range(8):
        a=ans<<3|t
        if a == 0:
            continue
        b = a%8
        b = b^3
        c = a>>b
        b = b^c
        b = b^3
        if b%8 == program[-1]:
            sub = Solve(program[:-1],a)
            if sub is None:
                continue
            return sub
        
def PartBSolve(inputs):
    registers,program = inputs.split("\n\n")
    registers = registers.split("\n")
    A = int(registers[0].split()[2])
    B = int(registers[1].split()[2])
    C = int(registers[2].split()[2])

    program = program[9:].split(",")
    program = [int(x) for x in program]

    answer = Solve(program,0)
    return answer

    
        
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
