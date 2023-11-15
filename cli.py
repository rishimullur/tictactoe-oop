import logging
from logic import TicTacToeLogic

class TicTacToeCLI:
    def __init__(self, logic):
        self.logic = logic

    def play_game(self):
        board = self.logic.make_empty_board()
        winner = None
        char = 'X'
        logging.basicConfig(filename='logs/game.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)
        logging.info('New Game begin')
        print("Choose Type of Game: 1. Single Player 2.Two-Player")
        game_type = int(input("Option:"))
        if game_type == 1:
            print("Single Player Mode selected!")
        elif game_type == 2:
            print("Two Player Mode Selected!")

        while winner is None:
            print("-------------------------------------")
            logging.info("Turn Begins")
            print("Begin Turn!")
            print("It's", char, "turn!")
            self.logic.show_current_board(board=board)
            print("Enter the row and column of the board you want to add the move to:")
            i = int(input("Enter the row number (Options- 1 | 2 | 3):"))
            j = int(input("Enter the column (Options- 1 | 2 | 3):"))
            board, is_illegal = self.logic.update_board(board=board, i=i, j=j, char=char)
            # if an illegal move happens, do not change the turn
            if not is_illegal:
                char = self.logic.other_player(player=char)
            winner = self.logic.get_winner(board)
            if winner == 'Draw':
                print("Game Draw")
            else:
                logging.info("Winner")


if __name__ == '__main__':
    logic = TicTacToeLogic()
    cli = TicTacToeCLI(logic)
    cli.play_game()

