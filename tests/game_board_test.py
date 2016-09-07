from unittest import TestCase
from game_board import GameBoard, Piece, COLORS, SHAPES, InvalidPlayException


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

    def test_playing_pieces_and_expanding_board(self):
        board = GameBoard()
        piece = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        board.play(piece)
        board.play(piece, x=1, y=2)
        board.play(piece, x=1, y=3)
        board.play(piece, x=1, y=4)
        board.play(piece, x=2, y=2)
        board.play(piece, x=3, y=2)
        board.play(piece, x=4, y=2)
        board.play(piece, x=0, y=2)
        board.play(piece, x=0, y=2)
        board.play(piece, x=0, y=2)
        board.play(piece, x=1, y=1)
        board.play(piece, x=1, y=0)
        board.play(piece, x=1, y=0)
        board.play(piece, x=1, y=0)

        expected_board = [
            [None, None, None, None, None, None, None, None, None, ],
            [None, piece, None, None, None, None, None, None, None, ],
            [None, piece, None, None, None, None, None, None, None, ],
            [None, piece, None, None, None, None, None, None, None, ],
            [None, piece, None, None, piece, None, None, None, None, ],
            [None, piece, piece, piece, piece, piece, piece, piece, None, ],
            [None, None, None, None, piece, None, None, None, None, ],
            [None, None, None, None, piece, None, None, None, None, ],
            [None, None, None, None, None, None, None, None, None, ],
        ]

        self.assertEqual(expected_board, board._board)

    def test_raises_placement_error_when_placing_on_edge_of_board(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        with self.assertRaises(InvalidPlayException):
            board.play(piece, x=0, y=0)
