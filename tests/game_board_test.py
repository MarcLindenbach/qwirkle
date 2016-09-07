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

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_right(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        board.play(piece, x=2, y=1)

        self.assertEqual(3, len(board._board))
        self.assertEqual(4, len(board._board[0]))
        self.assertEqual(piece, board._board[1][2])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_left(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        board.play(piece, x=0, y=1)

        self.assertEqual(3, len(board._board))
        self.assertEqual(4, len(board._board[0]))
        self.assertEqual(piece, board._board[1][1])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_up(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        board.play(piece, x=1, y=0)

        self.assertEqual(4, len(board._board))
        self.assertEqual(3, len(board._board[0]))
        self.assertEqual(piece, board._board[1][1])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_down(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        board.play(piece, x=1, y=2)

        self.assertEqual(4, len(board._board))
        self.assertEqual(3, len(board._board[0]))
        self.assertEqual(piece, board._board[2][1])
        
