from game_board import GameBoard, Piece, SHAPES, COLORS, InvalidPlayException
from player import Player


class QwirkleGame:
    def __init__(self):
        self._bag_of_tiles = []
        self._players = []
        self._board = []

    def main(self):

        self._board = GameBoard()
        self._generate_new_bag_of_tiles()

        print('Qwirkle Time!')

        self._players = [Player('Player 1'), Player('Player 2')]

        current_player = 0
        while True:
            print('%s Turn!', self._players[current_player].name())

            self._players[current_player].pick_tiles(self._bag_of_tiles)
            self._board.start_turn()
            self._players[current_player].play_turn(self._board)
            self._players[current_player].add_points(self._board.score())

            print('%s got %i points!' % (self._players[current_player].name(), self._board.score()))

            self._board.end_turn()
            self._players[current_player].pick_tiles(self._bag_of_tiles)

            for i in range(len(self._players)):
                print('%s - %i' % (self._players[i].name(), self._players[i].score()))

            if self._players[current_player].has_no_tiles():
                break;

            current_player += 1
            if current_player >= len(self._players):
                current_player = 0

        winning_player = max(self._players, key=lambda p: p.score())

        print('%s wins!' % winning_player.name())

    def _generate_new_bag_of_tiles(self):
        self._bag_of_tiles = []

        shapes = [
            SHAPES.CIRCLE,
            SHAPES.DIAMOND,
            SHAPES.SPARKLE,
            SHAPES.SQUARE,
            SHAPES.STAR,
            SHAPES.TRIANGLE
        ]

        colors = [
            COLORS.BLUE,
            COLORS.CYAN,
            COLORS.GREEN,
            COLORS.MAGENTA,
            COLORS.RED,
            COLORS.YELLOW
        ]

        for i in range(3):
            for c in range(len(colors)):
                for s in range(len(shapes)):
                    self._bag_of_tiles.append(Piece(color=colors[c], shape=shapes[s]))