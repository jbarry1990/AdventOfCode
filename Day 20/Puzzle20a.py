"""
Puzzle #20a - AdventOfCode
1. Read in image fragments
2. Store them in a a dictionary with the key being their ID
3. Determine the proper order and placement of each fragment to complete the
   larger image
4. Multiply the ID's of the 4 corner fragments together
5. Output the result
"""
  
from time import time

def ReadInFile():
    ImageFragments = {}
    Line = []
    Fragment = []
    
    File = open("./PuzzleInput.txt", "r")
    Key = ""
    for Entry in File:
        if Entry.strip().startswith("Tile"):
            Key = Entry[5:-2]
            continue
        if Entry == "\n":
            ImageFragments[Key] = Fragment
            Fragment = []
            continue
        else:
            for Character in Entry.strip():
                Line.append(Character)
            Fragment.append(Line)
            Line = []

        ImageFragments[Key] = Fragment
                
    return ImageFragments

def DetermineBorders(ImageFragments):
    Borders = {}

    ImageLength = len(ImageFragments["2477"])
    ImageWidth = len(ImageFragments["2477"][0])
    
    for Image in ImageFragments:
        Sides = []        
        Sides.append("".join(ImageFragments[Image][0]))
        Sides.append("".join(ImageFragments[Image][ImageLength-1]))
        Left = []
        Right = []
        for Index in range(ImageLength):
            Left.append(ImageFragments[Image][Index][0])
            Right.append(ImageFragments[Image][Index][ImageWidth-1])
        Sides.append("".join(Left))
        Sides.append("".join(Right))
        
        Borders[Image] = Sides

    return Borders

def SortPieces(Borders,ImageFragments):

    Corners = {}
    Outside = {}
    Inside = {}
    Matches = {}

    for Image in Borders:

        Top = Borders[Image][0]
        Left = Borders[Image][2]
        Right = Borders[Image][3]
        Bottom = Borders[Image][1]
        NumberOfMatches = 0
        
        for ComparedImage in Borders:

            if Image == ComparedImage:
                continue

            for Side in Borders[ComparedImage]:
                Reversed = Side[::-1]

                if Top == Side:

                    NumberOfMatches += 1
                    
                if Top == Reversed:

                    NumberOfMatches += 1
                    
                if Bottom == Side:

                    NumberOfMatches += 1

                if Bottom == Reversed:

                    NumberOfMatches += 1
                    
                if Left == Side:

                    NumberOfMatches += 1

                if Left == Reversed:

                    NumberOfMatches += 1
                    
                if Right == Side:

                    NumberOfMatches += 1

                if Right == Reversed:

                    NumberOfMatches += 1
                
        if NumberOfMatches == 4:
            Inside[Image] = ImageFragments[Image]
        if NumberOfMatches == 3:
            Outside[Image] = ImageFragments[Image]
        if NumberOfMatches == 2:
            Corners[Image] = ImageFragments[Image]
      
    return Inside, Outside, Corners

def MultiplyCorners(Corners):
    Answer = 1
    for Key in Corners:
        Answer *= int(Key)
        
    return Answer

def main():
    t_start = time()
    
    ImageFragments = ReadInFile()
    Borders = DetermineBorders(ImageFragments)
    Inside, Outside, Corners = SortPieces(Borders,ImageFragments)
    Answer = MultiplyCorners(Corners)

    print("Part 1: ", Answer)
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
