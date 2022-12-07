"""
Puzzle #22a - AdventOfCode
1. Read in each players hand
2. Play the game with the following Rules:
    1. Each player flips over their top card the one that is higher wins the round. Unless the value on the card is less than or equal to the remaining cards in that players deck.
       If this is true for both players a new game is started to determine the winner of the previous round. Each deck for the new game will contain the number of cards equal to the value
       of the cards flipped in the main game. Whoever wins this game wins the round in the main game.
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
    PlayerOneConfigurations = []
    PlayerTwoConfigurations = []
    Winner = []
    PlayerNumber = 0
    PlayGameFlag = True
    
    while PlayGameFlag == True:

        Player1Config = ",".join([str(Number) for Number in PlayerOne])
        Player2Config = ",".join([str(Number) for Number in PlayerTwo])
    
        if Player1Config in PlayerOneConfigurations or Player2Config in PlayerTwoConfigurations:
            Winner = PlayerOne
            PlayerNumber = 1
            return Winner, PlayerNumber
        else:
            PlayerOneConfigurations.append(Player1Config)
            PlayerTwoConfigurations.append(Player2Config)

        PlayerOneCard = PlayerOne.pop(0)
        PlayerTwoCard = PlayerTwo.pop(0)

        PlayerOneCardCount = len(PlayerOne)
        PlayerTwoCardCount = len(PlayerTwo)

        if PlayerOneCard <= PlayerOneCardCount and PlayerTwoCard <= PlayerTwoCardCount:
            PlayerOneDeck = PlayerOne[:PlayerOneCard]
            PlayerTwoDeck = PlayerTwo[:PlayerTwoCard]

            Winner, PlayerNumber = PlayGame(PlayerOneDeck, PlayerTwoDeck)            

            if PlayerNumber == 1:
                PlayerOne.append(PlayerOneCard)
                PlayerOne.append(PlayerTwoCard)
            else:
                PlayerTwo.append(PlayerTwoCard)
                PlayerTwo.append(PlayerOneCard)
        else:

            if PlayerOneCard > PlayerTwoCard:
                PlayerOne.append(PlayerOneCard)
                PlayerOne.append(PlayerTwoCard)
            else:
                PlayerTwo.append(PlayerTwoCard)
                PlayerTwo.append(PlayerOneCard)

        if len(PlayerOne) == 0:
            PlayGameFlag = False
            Winner = PlayerTwo
            PlayerNumber = 2

        if len(PlayerTwo) == 0:
            PlayGameFlag = False
            Winner = PlayerOne
            PlayerNumber = 1
            
    return Winner, PlayerNumber

def TabulateScore(Winner):
    Score = 0
    for Index in range(len(Winner)):
        Score += Winner[Index] * (len(Winner)-Index)
        
    return Score
def main():
    t_start = time()

    PlayerOne, PlayerTwo = ReadInFile()
    Winner, PlayerNumber = PlayGame(PlayerOne, PlayerTwo)
    Answer = TabulateScore(Winner)

    print("Player", PlayerNumber, "wins! Score: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
