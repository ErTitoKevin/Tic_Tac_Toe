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
def print_board():
    board_string = board_template.format(*board.values())
    return board_string



#Reads the players input
def read_choice():
    choice = input("Choose your move: ")
    while True:
        coord = choice
        if coord not in board:
            choice = input("Your input was not valid, please try again: ")
            continue
        if board[coord] != blank:
            choice = input("The move you choose already exists, please try again: ")
            continue
        if coord in board:
            return coord
#Defines who won the game, or if its a tie
def get_winner():
  if blank not in board.values():
    return "TIE"
  for combo in winning_combos:
      key1, key2, key3 = combo
      val1 = board[key1]
      val2 = board[key2]
      val3 = board[key3]
      if val1 == val2 == val3:
          if val1 in (x,o):
              return val1
#Places the chosen piece into the make_board_string
def play_game():
    print(print_board())
    while True:
        coordinate = read_choice()
        board[coordinate] = x
        print(print_board())
        winner = get_winner()
        if winner == "TIE":
            return "The Game is a Tie!"
        if winner in (x,o):
            win_message = winner + " has won the game!!"
            return win_message

def make_ai_choice():
    return "a_1"

print(play_game())

