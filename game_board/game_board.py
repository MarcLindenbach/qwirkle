from termcolor import colored
from game_board.invalid_play import InvalidPlayException


class GameBoard:

    def __init__(self):
        self._board = []

    def play(self, piece, x=0, y=0):
        if len(self._board) == 0:
            self._board = [[None] * 3 for i in range(3)]
            self._board[1][1] = piece
            return

        if self._is_invalid_play(piece, x, y):
            raise InvalidPlayException()

        self._board[y][x] = piece
        self._pad_board()

    def _is_invalid_play(self, piece, x, y):
        """Validates a move is within the board, not on the corners, and valid in its row/column"""
        if x < 0 or x >= len(self._board[0]):
            return True

        if y < 0 or y >= len(self._board):
            return True

        if x == 0 and y == 0:
            return True

        if x == 0 and y == len(self._board) - 1:
            return True

        if x == len(self._board[0]) - 1 and y == len(self._board) - 1:
            return True

        if x == len(self._board[0]) - 1 and y == 0:
            return True

        return False

    def _pad_board(self):
        """Ensures there is a padding of empty spots around the board"""

        # Check for top padding
        if any(self._board[0][i] is not None for i in range(len(self._board[0]))):
            self._board.insert(0, [None] * (len(self._board[0])))

        # Check for bottom padding
        bottom = len(self._board) - 1
        if any(self._board[bottom][i] is not None for i in range(len(self._board[0]))):
            self._board += [[None] * (len(self._board[0]))]

        # Left padding
        if any(self._board[i][0] is not None for i in range(len(self._board))):
            for i in range(len(self._board)):
                self._board[i].insert(0, None)

        # Right padding
        right = len(self._board[0]) - 1
        if any(self._board[i][right] is not None for i in range(len(self._board))):
            for i in range(len(self._board)):
                self._board[i] += [None]

    def _print_board(self):
        for y in range(len(self._board)):
            line = ''
            for x in range(len(self._board[y])):
                if self._board[y][x] is not None:
                    line += colored(self._board[y][x].shape, self._board[y][x].color)
                else:
                    line += '░'

            print(line)
