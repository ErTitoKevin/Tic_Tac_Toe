x = "X"
o = "O"
x_move = []
o_move = []
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


def get_winner():
  if blank not in board.values():
    return "TIE"
  for combo in winning_combos:
      key1, key2, key3 = combo
      if board[key1, key2, key3] == (x,o):
          return (x,o)




#Places the chosen piece into the make_board_string
def play_game():
    print(make_board_string())
    while True:
        coordinate, piece = read_choice()
        board[coordinate] = piece
        print(make_board_string())
        winner = get_winner()
        if winner == "TIE":
            return "The Game is a Tie!"
        if winner in (x,o):
            win_message = winner + " has won the game!!"
            return win_message


print(play_game())






