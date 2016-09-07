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
        piece1 = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        piece2 = Piece(color=COLORS.GREEN, shape=SHAPES.SPARKLE)
        board.play(piece1)

        board.play(piece2, x=2, y=1)

        self.assertEqual(3, len(board._board))
        self.assertEqual(4, len(board._board[0]))
        self.assertEqual(piece2, board._board[1][2])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_left(self):
        board = GameBoard()
        piece1 = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        piece2 = Piece(color=COLORS.GREEN, shape=SHAPES.SPARKLE)
        board.play(piece1)

        board.play(piece2, x=0, y=1)

        self.assertEqual(3, len(board._board))
        self.assertEqual(4, len(board._board[0]))
        self.assertEqual(piece2, board._board[1][1])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_up(self):
        board = GameBoard()
        piece1 = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        piece2 = Piece(color=COLORS.GREEN, shape=SHAPES.SPARKLE)
        board.play(piece1)

        board.play(piece2, x=1, y=0)

        self.assertEqual(4, len(board._board))
        self.assertEqual(3, len(board._board[0]))
        self.assertEqual(piece2, board._board[1][1])

    def test_playing_piece_adds_piece_to_board_at_correct_position_and_expands_board_down(self):
        board = GameBoard()
        piece1 = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        piece2 = Piece(color=COLORS.GREEN, shape=SHAPES.SPARKLE)
        board.play(piece1)

        board.play(piece2, x=1, y=2)

        self.assertEqual(4, len(board._board))
        self.assertEqual(3, len(board._board[0]))
        self.assertEqual(piece2, board._board[2][1])

    def test_playing_pieces_and_expanding_board(self):
        board = GameBoard()
        piece1 = Piece(color=COLORS.RED, shape=SHAPES.SPARKLE)
        piece2 = Piece(color=COLORS.RED, shape=SHAPES.SQUARE)
        piece3 = Piece(color=COLORS.RED, shape=SHAPES.CIRCLE)
        piece5 = Piece(color=COLORS.GREEN, shape=SHAPES.SQUARE)
        piece6 = Piece(color=COLORS.BLUE, shape=SHAPES.SQUARE)
        piece7 = Piece(color=COLORS.CYAN, shape=SHAPES.SQUARE)
        piece8 = Piece(color=COLORS.YELLOW, shape=SHAPES.SQUARE)
        piece9 = Piece(color=COLORS.MAGENTA, shape=SHAPES.SQUARE)
        piece10 = Piece(color=COLORS.MAGENTA, shape=SHAPES.SPARKLE)
        piece11 = Piece(color=COLORS.MAGENTA, shape=SHAPES.CIRCLE)
        piece12 = Piece(color=COLORS.MAGENTA, shape=SHAPES.STAR)
        piece13 = Piece(color=COLORS.MAGENTA, shape=SHAPES.TRIANGLE)
        piece14 = Piece(color=COLORS.MAGENTA, shape=SHAPES.DIAMOND)

        board.play(piece1)
        board.play(piece2, x=1, y=2)
        board.play(piece3, x=1, y=3)
        board.play(piece5, x=2, y=2)
        board.play(piece6, x=3, y=2)
        board.play(piece7, x=4, y=2)
        board.play(piece8, x=0, y=2)
        board.play(piece9, x=0, y=2)
        board.play(piece10, x=1, y=1)
        board.play(piece11, x=1, y=0)
        board.play(piece12, x=1, y=0)
        board.play(piece13, x=1, y=0)
        board.play(piece14, x=1, y=0)

        expected_board = [
            [None, None, None, None, None, None, None, None, ],
            [None, piece14, None, None, None, None, None, None ],
            [None, piece13, None, None, None, None, None, None],
            [None, piece12, None, None, None, None, None, None ],
            [None, piece11, None, None, None, None, None, None ],
            [None, piece10, None, piece1, None, None, None, None, ],
            [None, piece9, piece8, piece2, piece5, piece6, piece7, None, ],
            [None, None, None,  piece3, None, None, None, None, ],
            [None, None, None, None, None, None, None, None, ],
        ]

        self.assertEqual(expected_board, board._board)

    def test_raises_placement_error_when_placing_on_edge_of_board(self):
        board = GameBoard()
        piece = Piece()
        board.play(piece)

        with self.assertRaises(InvalidPlayException):
            board.play(piece, x=0, y=0)

    def test_raises_placement_error_when_placing_invalid_tiles_adjacent_horizontally(self):
        board = GameBoard()
        red_circle = Piece(shape=SHAPES.CIRCLE, color=COLORS.RED)
        board.play(red_circle)

        green_circle = Piece(shape=SHAPES.CIRCLE, color=COLORS.GREEN)
        board.play(green_circle, x=0, y=1)

        green_triangle = Piece(shape=SHAPES.TRIANGLE, color=COLORS.GREEN)

        with self.assertRaises(InvalidPlayException):
            board.play(green_triangle, x=0, y=1)

    def test_raises_placement_error_when_placing_invalid_tiles_adjacent_vertically(self):
        board = GameBoard()
        red_circle = Piece(shape=SHAPES.CIRCLE, color=COLORS.RED)
        board.play(red_circle)

        green_circle = Piece(shape=SHAPES.CIRCLE, color=COLORS.GREEN)
        board.play(green_circle, x=1, y=2)

        green_triangle = Piece(shape=SHAPES.TRIANGLE, color=COLORS.GREEN)

        with self.assertRaises(InvalidPlayException):
            board.play(green_triangle, x=1, y=3)
