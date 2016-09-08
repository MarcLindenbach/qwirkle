from termcolor import colored
import copy
from game_board.exceptions import InvalidPlayException


class GameBoard:

    def __init__(self):
        self._board = []
        self._plays = []

    def reset_board(self):
        """Clear the current board"""
        self._board = []
        self._plays = []

    def start_turn(self):
        """Start a turn"""
        self._plays = []

    def valid_plays(self):
        """Returns the valid plays"""
        valid_plays = []

        if not self._board:
            return [(0, 0)]

        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                if self._is_play_valid(None, x, y):
                    valid_plays.append((x, y))
        return valid_plays

    def get_board(self):
        """Return the current board with current moves"""
        return self._board

    def get_plays(self):
        return self._plays

    def play(self, piece, x=1, y=1):
        """Play a tile"""
        if len(self._board) == 0:
            self._board = [[None] * 3 for i in range(3)]
            x = 1
            y = 1
        else:
            if not self._is_play_valid(piece, x, y):
                raise InvalidPlayException()

        self._board[y][x] = piece
        self._plays.append((x, y, piece))
        self._pad_board()

    def score(self):
        """Return the score for the current turn"""
        if len(self._plays) == 0:
            return 0

        score = 0
        scored_horizontally = []
        scored_vertically = []

        for play in self._plays:
            x, y, piece = play

            min_x = x
            while min_x - 1 >= 0 and self._board[y][min_x - 1] is not None:
                min_x -= 1

            max_x = x
            while max_x + 1 < len(self._board[y]) and self._board[y][max_x + 1] is not None:
                max_x += 1

            if min_x != max_x:
                qwirkle_count = 0
                for t_x in range(min_x, max_x + 1):
                    if (t_x, y) not in scored_horizontally:
                        score += 1
                        qwirkle_count += 1
                        scored_horizontally.append((t_x, y))

                        if (x, y) not in scored_horizontally:
                            score += 1
                            qwirkle_count += 1
                            scored_horizontally.append((x, y))
                    t_x += 1

                if qwirkle_count == 6:
                    score += 6

            min_y = y
            while min_y - 1 >= 0 and self._board[min_y - 1][x] is not None:
                min_y -= 1

            max_y = y
            while max_y + 1 < len(self._board) and self._board[max_y + 1][x] is not None:
                max_y += 1

            if min_y != max_y:
                qwirkle_count = 0
                for t_y in range(min_y, max_y + 1):
                    if (x, t_y) not in scored_vertically:
                        score += 1
                        qwirkle_count += 1
                        scored_vertically.append((x, t_y))

                        if (x, y) not in scored_vertically:
                            score += 1
                            qwirkle_count += 1
                            scored_vertically.append((x, y))
                    t_y += 1

                if qwirkle_count == 6:
                    score += 6

        return score

    def end_turn(self):
        """End the current turn"""
        self._plays = []

    def reset_turn(self):
        """Reset the board to the way it was at the beginning of the turn"""
        for (x, y, tile) in self._plays:
            self._board[y][x] = None

        if all([self._board[y][x] is None for x in range(len(self._board[y])) for y in range(len(self._board))]):
            self._board = []

        self._plays = []

    def print_board(self):
        if len(self._board) == 0:
            print('  A')
            print('1', colored('■', 'white'))
            return

        valid_plays = self.valid_plays()
        lines = []
        for y in range(len(self._board)):
            line = ''
            for x in range(len(self._board[y])):
                if self._board[y][x] is not None:
                    line += colored(self._board[y][x].shape, self._board[y][x].color) + ' '
                elif (x, y) in valid_plays:
                    line += colored('■', 'white', attrs=['blink']) + ' '
                else:
                    line += '  '

            lines.append(line)

        # add in the top coord line
        line = ''.join([chr(65 + i) + ' ' for i in range(len(self._board[0]))])
        lines.insert(0, line)

        for i in range(0, len(lines)):
            i_display = i if i > 0 else ' '
            print(i_display, lines[i])

    @staticmethod
    def coord_to_position(coord):
        x_coord = ord(coord[0]) - 65
        y_coord = int(coord[1:]) - 1

        return x_coord, y_coord

    def _is_play_valid(self, piece, x, y):
        """Validates a move is within the board, not on the corners, not
           replacing a existing piece, adjacent to an existing tile and valid in
           its row/column"""

        # Make sure the placement is not on a corner and is inside the board
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

        # Make sure the placement is not already taken
        if self._board[y][x] is not None:
            return False

        # Make sure the placement has at least one adjacent placement
        adjacent_checks = []
        if y - 1 >= 0:
            adjacent_checks.append((self._board[y - 1][x] is None))
        if y + 1 < len(self._board):
            adjacent_checks.append((self._board[y + 1][x] is None))
        if x - 1 >= 0:
            adjacent_checks.append((self._board[y][x - 1] is None))
        if x + 1 < len(self._board[y]):
            adjacent_checks.append((self._board[y][x + 1] is None))

        if all(adjacent_checks):
            return False

        # Validate the play connects to an existing play
        plays = [(play[0], play[1]) for play in self._plays]
        if len(plays) > 0:
            check_horizontal = True
            check_vertical = True
            if len(plays) > 1:
                if plays[0][0] == plays[1][0]:
                    check_horizontal = False
                if plays[0][1] == plays[1][1]:
                    check_vertical = False

            in_plays = False

            if check_horizontal:
                t_x = x
                while t_x - 1 >= 0 and self._board[y][t_x - 1] is not None:
                    t_x -= 1
                    if (t_x, y) in plays:
                        in_plays = True

                t_x = x
                while t_x + 1 < len(self._board[y]) and self._board[y][t_x + 1] is not None:
                    t_x += 1
                    if (t_x, y) in plays:
                        in_plays = True

            if check_vertical:
                t_y = y
                while t_y - 1 >= 0 and self._board[t_y - 1][x] is not None:
                    t_y -= 1
                    if (x, t_y) in plays:
                        in_plays = True

                t_y = y
                while t_y + 1 < len(self._board) and self._board[t_y + 1][x] is not None:
                    t_y += 1
                    if (x, t_y) in plays:
                        in_plays = True

            if not in_plays:
                return False

        # Don't test for piece shape/color if no piece provided
        if piece is None:
            return True

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
            self._plays = [(play[0], play[1]+1, play[2]) for play in self._plays]

        # Check for bottom padding
        bottom = len(self._board) - 1
        if any(self._board[bottom][i] is not None for i in range(len(self._board[0]))):
            self._board += [[None] * (len(self._board[0]))]

        # Left padding
        if any(self._board[i][0] is not None for i in range(len(self._board))):
            for i in range(len(self._board)):
                self._board[i].insert(0, None)
            self._plays = [(play[0] + 1, play[1], play[2]) for play in self._plays]

        # Right padding
        right = len(self._board[0]) - 1
        if any(self._board[i][right] is not None for i in range(len(self._board))):
            for i in range(len(self._board)):
                self._board[i] += [None]

