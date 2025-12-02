import math

def ReadFile(filename):
    content = open(filename).read().strip()
    return content

    return content

def Solve(a,b,n):
    solutions = []
    i = 0
    while n>=a*i:
        if (n - (i * a)) % b == 0:
            solutions.append((i,int((n - (i * a)) / b)))
        i+=1
    return solutions
            
def PartASolve(inputs):
    Machines = inputs.split("\n\n")
    TokenA = 0
    TokenB = 0
    for m in Machines:
        a,b,prize = m.split("\n")
        aw = a.split()
        ax = int(aw[2].split('+')[1].split(',')[0])
        ay = int(aw[3].split('+')[1].split(',')[0])
        bw = b.split()
        bx = int(bw[2].split('+')[1].split(',')[0])
        by = int(bw[3].split('+')[1].split(',')[0])
        pw = prize.split()
        px = int(pw[1].split('=')[1].split(',')[0])
        py = int(pw[2].split('=')[1])

        if px%math.gcd(ax,bx) != 0 or py%math.gcd(ay,by) != 0:
            continue

        A = Solve(ax,bx,px)
        B = Solve(ay,by,py)

        x0= 0
        y0= 0
        for i in A:
            if i in B:
                x,y = i
                TokenA +=3*x
                TokenB +=y
                
            
            
            
    return TokenA+TokenB

def PartBSolve(inputs):
    Machines = inputs.split("\n\n")
    total = 0
    for m in Machines:
        a,b,prize = m.split("\n")
        aw = a.split()
        ax = int(aw[2].split('+')[1].split(',')[0])
        ay = int(aw[3].split('+')[1].split(',')[0])
        bw = b.split()
        bx = int(bw[2].split('+')[1].split(',')[0])
        by = int(bw[3].split('+')[1].split(',')[0])
        pw = prize.split()
        px = int(pw[1].split('=')[1].split(',')[0])
        py = int(pw[2].split('=')[1])

        row1 = [ax,bx,px+10000000000000]
        row2 = [ay,by,py+10000000000000]

        for i in range(2,-1,-1):
            row1[i] /= row1[0]

        for i in range(2,-1,-1):
            row2[i] -= (row2[0]*row1[i])
            
        for i in range(2,0,-1):
            row2[i] /= row2[1]

        for i in range(2,-1,-1):
            row1[i] -= (row1[1]*row2[i])

        if abs(row1[2] - round(row1[2])) < 0.001 and abs(row2[2] - round(row2[2])) < 0.001:
            total += (3*row1[2]+row2[2])

    return total

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
