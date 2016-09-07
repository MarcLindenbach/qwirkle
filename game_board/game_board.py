from termcolor 

class GameBoard:

    def __init__(self):
        self._board = []

    def play(self, piece, x=0, y=0):
        if len(self._board) == 0:
            self._board = [[None] * 3 for i in range(3)]
            self._board[1][1] = piece

            return

        self._board[y][x] = piece
        self._pad_board()

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
                line += '▉' if self._board[y][x] is not None else '░'
            print(line)
