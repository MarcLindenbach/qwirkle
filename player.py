from random import Random
from termcolor import colored


class Player:
    def __init__(self, name='Unknown Player'):
        self._tiles = []
        self._score = 0
        self._name = name

    def pick_tiles(self, bag_of_tiles):
        rnd = Random()
        while len(self._tiles) < 6 and len(bag_of_tiles) > 0:
            i = rnd.randint(0, len(bag_of_tiles) - 1)

            self._tiles.append(bag_of_tiles.pop(i))

    def play_turn(self, board):
        tiles = self._tiles.copy()
        while True:
            board.print_board()
            self.print_tiles(tiles)
            print('Options')
            print(' "r"  to reset board')
            print(' "p# @#" to play a tile, where # is that tile, @ is the letter coord and # is the numeric coord')
            print(' "f" to finish turn')
            choice = input('--> ')

            if len(choice) == 0:
                continue

            if choice == 'r':
                board.reset_turn()
                tiles = self._tiles.copy()
                continue

            if choice == 'f':
                break

            if choice[0] != 'p':
                continue

            tile_index = int(choice[1]) - 1
            if tile_index >= len(tiles):
                continue

            x, y = board.coord_to_position(choice[3:])
            board.play(tiles.pop(tile_index), x, y)

    @staticmethod
    def print_tiles(tiles):
        tiles_output = ''
        for tile in tiles:
            tiles_output += colored(tile.shape, tile.color) + ' '
        print('Your Tiles: %s' % tiles_output)
        print('            1 2 3 4 5 6')

    def score(self):
        return self._score

    def add_points(self, points):
        self._score += points

    def has_no_tiles(self):
        return self._tiles == 0

    def name(self):
        return self._name
