"""
Puzzle #22b - AdventOfCode
"""
from time import time 
from itertools import cycle, islice


def move(current, right):
    removed = [right[current],
               right[right[current]],
               right[right[right[current]]]]
    right[current] = right[removed[-1]]
    destination = current
    while True:
        destination -= 1
        if destination == 0:
            destination = len(right)
        if destination not in removed:
            break
    right[removed[-1]] = right[destination]
    right[destination] = removed[0]
    return right[current]


def solve(cups, iterations):
    right = dict(zip(cups, cups[1:] + cups[:1]))
    current = cups[0]
    for _ in range(iterations):
        current = move(current, right)
    return right


# Part one
def main():
    cups = list(map(int, '589174263'))
    print(cups)

    # Part two
    cups += range(10, 1_000_001)
    right = solve(cups, 10_000_000)
    print(right[1] * right[right[1]])
    
if __name__ == "__main__":
    main()
