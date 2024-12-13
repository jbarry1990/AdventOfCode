def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    boards = []
    order = file_contents[0].strip().split(",")
    order = [int(i) for i in order]
    current_board = []
    for line in file_contents[2:]:
        if line == "\n":
            boards.append(current_board)
            current_board = []
            continue
        current_board.append(line.split())
    boards.append(current_board)
    
    return order, boards

def PartASolve(order, boards):
    bingos = {}
    winning_board = -1
    last_number_called = -1
    unmarked_numbers_sum = 0
    for index, board in enumerate(boards):
        bingos[index] = [[0,0,0,0,0],[0,0,0,0,0]]

    for number in order:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for column_index, column in enumerate(row):
                    if column == "X":
                        continue
                    if int(column) == number:
                        bingos[board_index][0][row_index] += 1
                        bingos[board_index][1][column_index] += 1
                        boards[board_index][row_index][column_index] = "X"

        for key in bingos:
            if 5 in bingos[key][0] or 5 in bingos[key][1]:
                winning_board = key
                break
        if winning_board != -1:
            last_number_called = number
            break

    for row in boards[winning_board]:
        for number in row:
            if number == "X":
                continue
            unmarked_numbers_sum += int(number)
                        
    return unmarked_numbers_sum * last_number_called

def PartBSolve(order, boards):
    bingos = {}
    losing_board = -1
    last_number_called = -1
    bingos = []
    unmarked_numbers_sum = 0
    for index, board in enumerate(boards):
        bingos.append([[0,0,0,0,0],[0,0,0,0,0]])

    for number in order:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for column_index, column in enumerate(row):
                    if column == "X":
                        continue
                    if int(column) == number:
                        bingos[board_index][0][row_index] += 1
                        bingos[board_index][1][column_index] += 1
                        boards[board_index][row_index][column_index] = "X"

        boards_to_remove = []
        for index, card in enumerate(bingos):
            if 5 in bingos[index][0] or 5 in bingos[index][1]:
                if len(boards) == 1:
                    losing_board = index
                    break
                else:
                    boards_to_remove.append(index)

        if len(boards) == 1:
            last_number_called = number
            break

             
        if len(boards_to_remove) != 0:
            for complete_board in reversed(boards_to_remove):
                boards.pop(complete_board)
                bingos.pop(complete_board)

    for row in boards[losing_board]:
        for number in row:
            if number == "X":
                continue
            unmarked_numbers_sum += int(number)
                        
    return unmarked_numbers_sum * last_number_called

def main():
    file_contents = ReadFile("Inputs.txt")
    order, boards = ParseFile(file_contents)
    answer = PartASolve(order, boards)
    print("Part A Answer: ", answer)
    order, boards = ParseFile(file_contents)
    answer = PartBSolve(order, boards)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
