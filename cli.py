# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, show_current_board ,update_board, other_player
import logging

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    # Intiazlize the first move to X
    char = 'X'
    logging.basicConfig(filename='logs/game.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' ,encoding='utf-8', level=logging.DEBUG)
    logging.info('New Game begin')

    while winner == None:
        print("-------------------------------------")
        logging.info("Turn Begins")
        print("Begin Turn!")
        print("It's", char, "turn!")
        show_current_board(board=board)
        print("Enter the row and column of the board you want to add the move to:")
        i = int(input("Enter the row number (Options- 1 | 2 | 3):"))
        j = int(input("Enter the column (Options- 1 | 2 | 3):"))
        board, is_illegal = update_board(board=board,i=i,j=j,char=char)
        #if an illegal move happens, do not change the turn
        if is_illegal!= True:
            char = other_player(player = char)
        winner = get_winner(board)
        if winner == 'Draw':
            print("Game Draw")
        else:
            logging.info("Winner")

