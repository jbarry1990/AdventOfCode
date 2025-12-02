def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def PartASolve(inputs):
    nums = [int(num) for num in inputs]
    final = []
    for num in nums:
        ns = num
        for _ in range(1999):
            s1 = ns*64
            s2 = s1^ns
            s3 = s2%16777216
            s4 = s3//32
            s5 = s4^s3
            s6 = s5%16777216
            s7 = s6*2048
            s8 = s6^s7
            ns = s8%16777216

        final.append(ns)
    return sum(final)

def PartBSolve(inputs):
    def step(num):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        return num

    seq_to_total = {}

    for line in inputs:
        num = int(line)
        buyer = [num % 10]
        for _ in range(2000):
            num = step(num)
            buyer.append(num % 10)
        seen = set()
        for i in range(len(buyer) - 4):
            a, b, c, d, e = buyer[i:i + 5]
            seq = (b - a, c - b, d - c, e - d)
            if seq in seen: continue
            seen.add(seq)
            if seq not in seq_to_total: seq_to_total[seq] = 0
            seq_to_total[seq] += e

    return max(seq_to_total.values())
            
        
        
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
