import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner_DRAW(self):
        board = [
            ['X', 'X', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'Draw')

    def test_get_winner(self):
        board_1 = [
            ['O', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board_1), 'X')

    def test_other_player(self):
        player = 'O'
        self.assertEqual(logic.other_player(player=player),'X')

    def test_update_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', None],
        ]
        test_case_board = ([['X', 'X', 'O'],[None, 'X', None],[None, 'O', None]],False)
        self.assertEqual(logic.update_board(board,i=1,j=2,char='X'),test_case_board)

if __name__ == '__main__':
    unittest.main()
