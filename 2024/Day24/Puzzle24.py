from collections import defaultdict, deque

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
        return content

def PartASolve(inputs):
    wires,ops = inputs.split("\n\n")
    wires = wires.split("\n")
    ops = ops.split("\n")
    
    wires = {wire.strip().split(": ")[0]:int(wire.strip().split(": ")[1]) for wire in wires}
    gates = []
    for op in ops:
        l,g,r,a,o = op.split()
        if l not in wires: wires[l] = None
        if r not in wires: wires[r] = None
        if o not in wires: wires[o] = None

        gates.append((l,r,g,o))

    while any(value is None for value in wires.values()):
        for l,r,g,o in gates:
            if wires[l] == None or wires[r] == None: continue
            if wires[o] != None: continue
            
            if g == "AND":
                wires[o] = wires[l] & wires[r]
            elif g == "OR":
                wires[o] = wires[l] | wires[r]
            elif g == "XOR":
                wires[o] = wires[l] ^ wires[r]
    outputs = {}
    for wire in wires:
        if wire.startswith("z"):
            outputs[wire] = wires[wire]

    outputs = sorted(list(outputs))

    result = 0
    for x,output in enumerate(outputs):
        result += wires[output]*2**x

    return result
        
        
def PartBSolve(inputs):
    wires,ops = inputs.split("\n\n")
    wires = wires.split("\n")
    ops = ops.split("\n")

    formulas = {}

    for line in ops:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

    def make_wire(char, num):
        return char + str(num).rjust(2, "0")

    def verify_z(wire, num):
        # print("vz", wire, num)
        if wire not in formulas: return False
        op, x, y = formulas[wire]
        if op != "XOR": return False
        if num == 0: return sorted([x, y]) == ["x00", "y00"]
        return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

    def verify_intermediate_xor(wire, num):
        # print("vx", wire, num)
        if wire not in formulas: return False
        op, x, y = formulas[wire]
        if op != "XOR": return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        # print("vc", wire, num)
        if wire not in formulas: return False
        op, x, y = formulas[wire]
        if num == 1:
            if op != "AND": return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != "OR": return False
        return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)

    def verify_direct_carry(wire, num):
        # print("vd", wire, num)
        if wire not in formulas: return False
        op, x, y = formulas[wire]
        if op != "AND": return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        # print("vr", wire, num)
        if wire not in formulas: return False
        op, x, y = formulas[wire]
        if op != "AND": return False
        return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

    def verify(num):
        return verify_z(make_wire("z", num), num)

    def progress():
        i = 0
        
        while True:
            if not verify(i): break
            i += 1
        
        return i

    swaps = []

    for _ in range(4):
        baseline = progress()
        for x in formulas:
            for y in formulas:
                if x == y: continue
                formulas[x], formulas[y] = formulas[y], formulas[x]
                if progress() > baseline:
                    break
                formulas[x], formulas[y] = formulas[y], formulas[x]
            else:
                continue
            break
        swaps += [x, y]

    print(",".join(sorted(swaps)))
             
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
