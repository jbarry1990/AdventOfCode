import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    # 1. Parse Input into a list of tuples
    # 2. Sort input into 7 types
    # 3. Sort each type by strength
    # 4. Determine score

    hands = [tuple(file.split()) for file in file_contents]
    hands = [(hand,int(bet)) for hand,bet in hands]
    hands_score = {hand:int(bet) for hand,bet in hands}
    hand = [h for h,b in hands]

    fivekind = []
    fourkind = []
    fullhouse = []
    threekind = []
    twopair = []
    onepair = []
    highcard = []
    types = [fivekind,fourkind,fullhouse,threekind,twopair,onepair,highcard]

    for hand,bet in hands:
        unique = set(list(hand))
        hand_list = list(hand)
        if len(unique) == 5:
            highcard.append((hand,bet))
        elif len(unique)== 4:
            onepair.append((hand,bet))
        elif len(unique)== 3:
            # either 3 of a kind, two pair
            hand_list = list(hand)
            for el in hand_list:
                if hand_list.count(el) == 3:
                    threekind.append((hand,bet))
                    break
            else:
                twopair.append((hand,bet))
        elif len(unique)== 2:
            # either full house or 4 of a kind
            hand_list = list(hand)
            for el in hand_list:
                if hand_list.count(el) == 4:
                    fourkind.append((hand,bet))
                    break
            else:
                fullhouse.append((hand,bet))
            
        elif len(unique)== 1:
            fivekind.append((hand,bet))

    ordered = []
    card_to_letter=dict(zip('23456789TJQKA','abcdefghijklm'))
    letter_to_card = dict(zip('abcdefghijklm','23456789TJQKA'))
    for t in types:
        if t == []:
            continue
        hands = [list(hand) for hand,bet in t]
        converted_list = [[card_to_letter[x] for x in y] for y in hands]
        sorted_list = ["".join(x) for x in converted_list]
        sorted_list.sort(reverse=True)
        sorted_list = [list(x) for x in sorted_list]
        final_list = [[letter_to_card[x] for x in y] for y in sorted_list]
        final_list = ["".join(x) for x in final_list]
        for i in final_list:
            ordered.append(i)

    answer = 0
    for i,order in enumerate(ordered[::-1]):        
        answer +=hands_score[order]*(i+1)

    return answer

def PartBSolve(file_contents):        
    # 1. Parse Input into a list of tuples
    hands = [tuple(file.split()) for file in file_contents]
    hands = [(hand,int(bet)) for hand,bet in hands]
    hands_score = {hand:int(bet) for hand,bet in hands}
    hand = [h for h,b in hands]

    fivekind = []
    fourkind = []
    fullhouse = []
    threekind = []
    twopair = []
    onepair = []
    highcard = []
    types = [fivekind,fourkind,fullhouse,threekind,twopair,onepair,highcard]

    # 2. Sort input into 7 types
    for hand,bet in hands:
        unique = set(list(hand))
        hand_list = list(hand)
        if len(unique) == 5:
            if "J" not in hand_list:
                highcard.append((hand,bet))
            elif hand_list.count("J")==1:
                onepair.append((hand,bet))
        elif len(unique)== 4:
            if "J" not in hand_list:
                onepair.append((hand,bet))
            elif hand_list.count("J") == 1:
                threekind.append((hand,bet))
            elif hand_list.count("J") == 2:
                threekind.append((hand,bet))
        elif len(unique)== 3:
            for el in hand_list:
                if hand_list.count(el) == 3:
                    if "J" not in hand_list:
                        threekind.append((hand,bet))
                    else:
                        fourkind.append((hand,bet))
                    break
            else:
                if "J" not in hand_list:
                    twopair.append((hand,bet))
                elif hand_list.count("J") == 1:
                    fullhouse.append((hand,bet))
                elif hand_list.count("J") == 2:
                    fourkind.append((hand,bet))
        elif len(unique)== 2:
            hand_list = list(hand)
            for el in hand_list:
                if hand_list.count(el) == 4:
                    if "J" not in hand_list:
                        fourkind.append((hand,bet))
                    else:
                        fivekind.append((hand,bet))
                    break
            else:
                if "J" not in hand_list:
                    fullhouse.append((hand,bet))
                else:
                    fivekind.append((hand,bet))
        elif len(unique)== 1:
            fivekind.append((hand,bet))
            
    # 3. Sort each type by strength
    ordered = []
    card_to_letter=dict(zip('J23456789TQKA','abcdefghijklm'))
    letter_to_card = dict(zip('abcdefghijklm','J23456789TQKA'))
    for t in types:
        if t == []:
            continue
        hands = [list(hand) for hand,bet in t]
        converted_list = [[card_to_letter[x] for x in y] for y in hands]
        sorted_list = ["".join(x) for x in converted_list]
        sorted_list.sort(reverse=True)
        sorted_list = [list(x) for x in sorted_list]
        final_list = [[letter_to_card[x] for x in y] for y in sorted_list]
        final_list = ["".join(x) for x in final_list]
        for i in final_list:
            ordered.append(i)

    # 4. Determine score            
    answer = 0
    for i,order in enumerate(ordered[::-1]):        
        answer +=hands_score[order]*(i+1)

    return answer

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
