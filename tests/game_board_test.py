from unittest import TestCase
from game_board import GameBoard, Piece


class GameBoardTest(TestCase):

    def test_initial_play_creates_3_x_3_board_with_piece_in_middle(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        self.assertEqual(3, len(board._board))
        self.assertEqual(3, len(board._board[0]))
        self.assertEqual(piece, board._board[1][1])
