"""
Puzzle #22a - AdventOfCode
1. Read in each players hand
2. Play the game with the following Rules:
    1. Each player flips over their top card the one that is higher wins the round.
    2. Take both cards and put them at the bottom of the deck with the higher card on top of the lower card.
    3. First person to have all of the cards wins
3. Score the winner. The bottom card of their deck is worth the value * 1 point the next is the value * 2 and so on and so forth
4. Output the score.
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Deck = []
    PlayerOne = []
    PlayerTwo = []

    for Lines in File:
        Deck.append(Lines.strip())
    
    PlayerOneDeck = True

    for Index, Cards in enumerate(Deck):
        if Cards.startswith("Player"):
            continue

        if Cards == "":
            PlayerOneDeck = False
            continue
        
        if PlayerOneDeck == True:
            PlayerOne.append(int(Cards))
        else:
            PlayerTwo.append(int(Cards))

    return PlayerOne, PlayerTwo

def PlayGame(PlayerOne, PlayerTwo):
    Winner = []
    PlayGame = True
    
    while PlayGame == True:
        PlayerOneCard = PlayerOne.pop(0)
        PlayerTwoCard = PlayerTwo.pop(0)

        if PlayerOneCard > PlayerTwoCard:
            PlayerOne.append(PlayerOneCard)
            PlayerOne.append(PlayerTwoCard)
        else:
            PlayerTwo.append(PlayerTwoCard)
            PlayerTwo.append(PlayerOneCard)

        if len(PlayerOne) == 0:
            PlayGame = False
            Winner = PlayerTwo

        if len(PlayerTwo) == 0:
            PlayGame = False
            Winner = PlayerOne
            
    return Winner

def TabulateScore(Winner):
    Score = 0
    for Index in range(len(Winner)):
        Score += Winner[Index] * (len(Winner)-Index)
        
    return Score
def main():
    t_start = time()

    PlayerOne, PlayerTwo = ReadInFile()
    Winner = PlayGame(PlayerOne, PlayerTwo)
    Answer = TabulateScore(Winner)

    print("Part 1: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
