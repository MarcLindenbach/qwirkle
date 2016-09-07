class GameBoard:

    def __init__(self):
        self._board = []

    def play(self, piece, x=0, y=0):

        if len(self._board) == 0:
            self._board = [[None] * 3 for i in range(3)]
            self._board[1][1] = piece

