x = "X"
o = "O"
blank = "-"
board = {"a_1": blank, "b_1": blank, "c_1": blank,
         "a_2": blank, "b_2": blank, "c_2": blank,
         "a_3": blank, "b_3": blank, "c_3": blank }
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
    user_choosing = True
    choice = input("Choose your move: ")
    while user_choosing:
        coord = choice[:3]  # Board Key
        x_or_o = choice[4:5]  # X or O choice
        if coord in board and x_or_o in (x, o):
            return coord, x_or_o
        else:
            choice = input("Your input was not valid, please try again: ")
#Places the chosen piece into the make_board_string
def place_piece():
    game_on = True
    while game_on:
        coordinate, piece = read_choice()
        board[coordinate] = piece
        print(make_board_string())
        if blank not in board.values():
            return "The gameboard is full"


print(place_piece())