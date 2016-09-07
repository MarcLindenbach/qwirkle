from termcolor import colored
from game_board.invalid_play import InvalidPlayException


class GameBoard:

    def __init__(self):
        self._board = []
        self._saved_board = []
        self._plays = []

    def reset_board(self):
        """Clear the current board"""
        pass

    def start_turn(self):
        """Start a turn"""
        self._board = self._saved_board.copy()
        self._plays = []

    def play(self, piece, x=1, y=1):
        """Play a tile"""
        if len(self._board) == 0:
            self._board = [[None] * 3 for i in range(3)]

        if not self._is_play_valid(piece, x, y):
            raise InvalidPlayException()

        self._board[y][x] = piece
        self._plays.append((x,y))
        self._pad_board()

    def score(self):
        """Return the score for the current turn"""
        pass

    def end_turn(self):
        """End the current turn"""
        self._saved_board = self._board.copy()
        self._plays = []

    def reset_turn(self):
        """Reset the board to the way it was at the beginning of the turn"""
        self._board = self._saved_board.copy()
        self._plays = []

    def _is_play_valid(self, piece, x, y):
        """Validates a move is within the board, not on the corners, not
           replacing a existing piece, adjacent to an existing tile and valid in
           its row/column"""
        if x < 0 or x >= len(self._board[0]):
            return False
        if y < 0 or y >= len(self._board):
            return False
        if x == 0 and y == 0:
            return False
        if x == 0 and y == len(self._board) - 1:
            return False
        if x == len(self._board[0]) - 1 and y == len(self._board) - 1:
            return False
        if x == len(self._board[0]) - 1 and y == 0:
            return False

        if self._board[y][x] is not None:
            return False

        # Get & Verify all the tiles adjacent horizontally
        row = [piece]
        t_x = x + 1
        while t_x < len(self._board[0]) and self._board[y][t_x] is not None:
            row.append(self._board[y][t_x])
            t_x += 1

        t_x = x - 1
        while t_x >= 0 and self._board[y][t_x] is not None:
            row.append(self._board[y][t_x])
            t_x -= 1

        if not self._is_row_valid(row):
            return False

        # Get & Verify all the tiles adjacent vertically
        row = [piece]
        t_y = y + 1
        while t_y < len(self._board) and self._board[t_y][x] is not None:
            row.append(self._board[t_y][x])
            t_y += 1

        t_y = y - 1
        while t_y >= 0 and self._board[t_y][x] is not None:
            row.append(self._board[t_y][x])
            t_y -= 1

        if not self._is_row_valid(row):
            return False

        return True

    def _is_row_valid(self, row):
        """If all row colors are equal, check each shape shows up at most once.
           If all shapes are equal, check each color shows up at most once.
           Otherwise the row is invalid."""

        if len(row) == 1:
            return True

        if all(row[i].color == row[0].color for i in range(len(row))):
            shapes = []
            for i in range(len(row)):
                if row[i].shape in shapes:
                    return False
                shapes.append(row[i].shape)

        elif all(row[i].shape == row[0].shape for i in range(len(row))):
            colors = []
            for i in range(len(row)):
                if row[i].color in colors:
                    return False
                colors.append(row[i].color)

        else:
            return False

        return True

    def _pad_board(self):
        """Ensures there is a padding of empty spots around the board, update the plays"""

        # Check for top padding
        if any(self._board[0][i] is not None for i in range(len(self._board[0]))):
            self._board.insert(0, [None] * (len(self._board[0])))
            self._plays = [(play[0], play[1]+1) for play in self._plays]

        # Check for bottom padding
        bottom = len(self._board) - 1
        if any(self._board[bottom][i] is not None for i in range(len(self._board[0]))):
            self._board += [[None] * (len(self._board[0]))]

        # Left padding
        if any(self._board[i][0] is not None for i in range(len(self._board))):
            for i in range(len(self._board)):
                self._board[i].insert(0, None)
            self._plays = [(play[0] + 1, play[1]) for play in self._plays]

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
