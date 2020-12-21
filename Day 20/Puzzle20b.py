"""
Puzzle #20a - AdventOfCode
1. Put the puzzle together. Remove the borders
2. Search for pattern in array.(May have to rotate or flip the image)
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

    ImageLength = len(ImageFragments["2311"])
    ImageWidth = len(ImageFragments["2311"][0])
    
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
            Inside[Image] = Borders[Image]
        if NumberOfMatches == 3:
            Outside[Image] = Borders[Image]
        if NumberOfMatches == 2:
            Corners[Image] = Borders[Image]
      
    return Inside, Outside, Corners

def DetermineFragmentLocation(Corners, Inside, Outside, ImageFragments):
    ImageLength = len(ImageFragments["2311"])
    ImageWidth = len(ImageFragments["2311"][0])
    OutsideMatches = {}
    InsideMatches = {}
    CornerMatches = {}
    Grid = {}
    for Image in Corners:
        Top = Corners[Image][0]
        Left = Corners[Image][2]
        Right = Corners[Image][3]
        Bottom = Corners[Image][1]

        Data = []
        for Neighbors in Outside:
            
            for Index, Side in enumerate(Outside[Neighbors]):
                Reversed = Side[::-1]
                
                
                if Top == Side:
                    Data.append(("Top", Neighbors, Index, False))
                if Top == Reversed:
                    Data.append(("Top",Neighbors, Index, True))
                if Bottom == Side:
                    Data.append(("Bottom", Neighbors, Index, False))
                if Bottom == Reversed:
                    Data.append(("Bottom", Neighbors, Index, True))
                if Left == Side:
                    Data.append(("Left", Neighbors, Index, False))
                if Left == Reversed:
                    Data.append(("Left",Neighbors, Index, True))
                if Right == Side:
                    Data.append(("Right",Neighbors, Index, False))
                if Right == Reversed:
                    Data.append(("Right",Neighbors, Index, True))
            CornerMatches[Image] = Data

    for Image in Outside:
        Top = Outside[Image][0]
        Left = Outside[Image][2]
        Right = Outside[Image][3]
        Bottom = Outside[Image][1]
        Data = []
        for Neighbors in Inside:
            
            for Index, Side in enumerate(Inside[Neighbors]):
                Reversed = Side[::-1]
                
                
                if Top == Side:
                    Data.append(("Top", Neighbors, Index, False))
                if Top == Reversed:
                    Data.append(("Top",Neighbors, Index, True))
                if Bottom == Side:
                    Data.append(("Bottom", Neighbors, Index, False))
                if Bottom == Reversed:
                    Data.append(("Bottom", Neighbors, Index, True))
                if Left == Side:
                    Data.append(("Left", Neighbors, Index, False))
                if Left == Reversed:
                    Data.append(("Left",Neighbors, Index, True))
                if Right == Side:
                    Data.append(("Right",Neighbors, Index, False))
                if Right == Reversed:
                    Data.append(("Right",Neighbors, Index, True))
            OutsideMatches[Image] = Data
            
        for Neighbors in Corners:
            
            for Index, Side in enumerate(Corners[Neighbors]):
                Reversed = Side[::-1]
                
                
                if Top == Side:
                    Data.append(("Top", Neighbors, Index, False))
                if Top == Reversed:
                    Data.append(("Top",Neighbors, Index, True))
                if Bottom == Side:
                    Data.append(("Bottom", Neighbors, Index, False))
                if Bottom == Reversed:
                    Data.append(("Bottom", Neighbors, Index, True))
                if Left == Side:
                    Data.append(("Left", Neighbors, Index, False))
                if Left == Reversed:
                    Data.append(("Left",Neighbors, Index, True))
                if Right == Side:
                    Data.append(("Right",Neighbors, Index, False))
                if Right == Reversed:
                    Data.append(("Right",Neighbors, Index, True))
            OutsideMatches[Image] = Data

    for Image in Inside:
        Top = Inside[Image][0]
        Left = Inside[Image][2]
        Right = Inside[Image][3]
        Bottom = Inside[Image][1]
        Data = []
        for Neighbors in Outside:
            
            for Index, Side in enumerate(Outside[Neighbors]):
                Reversed = Side[::-1]
                
                
                if Top == Side:
                    Data.append(("Top", Neighbors, Index, False))
                if Top == Reversed:
                    Data.append(("Top",Neighbors, Index, True))
                if Bottom == Side:
                    Data.append(("Bottom", Neighbors, Index, False))
                if Bottom == Reversed:
                    Data.append(("Bottom", Neighbors, Index, True))
                if Left == Side:
                    Data.append(("Left", Neighbors, Index, False))
                if Left == Reversed:
                    Data.append(("Left",Neighbors, Index, True))
                if Right == Side:
                    Data.append(("Right",Neighbors, Index, False))
                if Right == Reversed:
                    Data.append(("Right",Neighbors, Index, True))
            InsideMatches[Image] = Data
        
    return

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

    DetermineFragmentLocation(Corners, Inside, Outside,ImageFragments)
    Answer = MultiplyCorners(Corners)

    print("Part 1: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
