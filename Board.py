x = "X"
o = "O"
blank = "-"
board = {"a_1": blank, "b_1": blank, "c_1": blank,
         "a_2": blank, "b_2": blank, "c_2": blank,
         "a_3": blank, "b_3": blank, "c_3": blank }
winning_combos =[["a_1", "a_2", "a_3"],["b_1", "b_2", "b_3"],["c_1", "c_2", "c_3"],
                 ["a_1", "b_1", "c_1"],["a_2", "b_2", "c_2"],["a_3", "b_3", "c_3"],
                 ["a_1", "b_2", "c_3"],["a_3", "b_2", "c_1"]]
board_template = """
                                       a     b     c
                                          |     |     
                                    1  {}  |  {}  |  {} 
                                     _____|_____|_____
                                          |     |     
                                    2  {}  |  {}  |  {}
                                     _____|_____|_____
                                          |     |     
                                    3  {}  |  {}  |  {}
                                          |     |     
                                                            """
#Creates the basic playing board
def make_board_string():
    board_string = board_template.format(*board.values())
    return board_string
#Reads the players input
def read_choice():
    choice = input("Choose your move: ")
    while True:
        coord = choice[:3]  # Board Key
        x_or_o = choice[4:5]  # X or O choice
        if coord in board and x_or_o in (x, o):
            return coord, x_or_o
        else:
            choice = input("Your input was not valid, please try again: ")
#Places the chosen piece into the make_board_string
def place_piece():
    while True:
        coordinate, piece = read_choice()
        board[coordinate] = piece
        print(make_board_string())
        if blank not in board.values():
            return "The Game is a Tie!"


print(place_piece())

for winning_comb in winning_combos:
    for comb in winning_comb:
        if comb in coordinate:
            winner = piece + " has won Tic_Tac_toe!!"
            return winner