from game_board import GameBoard, Piece, SHAPES, COLORS, InvalidPlayException
from player import Player
from bots import GreedyBot, SingleGreedyBot


class QwirkleGame:
    def __init__(self):
        self._bag_of_tiles = []
        self._players = []
        self._board = []

    def main(self, players):

        self._board = GameBoard()
        self._generate_new_bag_of_tiles()

        player_number = 1
        for player in players:
            if player == 'greedy_bot':
                self._players.append(GreedyBot('Player %i' % player_number))
            elif player == 'single_greedy_bot':
                self._players.append(SingleGreedyBot('Player %i' % player_number))
            elif player == 'human':
                self._players.append(Player('Player %i' % player_number))
            else:
                raise ValueError('%s is an invalid player type' % player)
            player_number += 1

        score_message = (-1, 0)
        current_player = 0
        while True:
            print('\n' * 50)
            print('Qwirkle Hard\n')

            print('  Score:')
            for i in range(len(self._players)):
                message = '    %s - %i' % (self._players[i].name(), self._players[i].score())
                if score_message[0] == i:
                    message += ' +%i' % score_message[1]
                print(message)
            print('\n  It is %ss turn\n' % self._players[current_player].name())

            self._board.print_board()
            self._players[current_player].pick_tiles(self._bag_of_tiles)
            self._board.start_turn()
            self._players[current_player].play_turn(self._board)

            score = self._board.score()
            self._players[current_player].add_points(score)

            score_message = (current_player, score)
            self._board.end_turn()

            if score == 0:
                print('  %s is exchanging tiles...' % self._players[current_player].name())
                self._bag_of_tiles += self._players[current_player].get_tiles()
                self._players[current_player].clear_tiles()

            self._players[current_player].pick_tiles(self._bag_of_tiles)

            if self._players[current_player].has_no_tiles():
                break

            current_player += 1
            if current_player >= len(self._players):
                current_player = 0

        winning_player = max(self._players, key=lambda p: p.score())

        print('\n  Final Score:')
        for i in range(len(self._players)):
            message = '    %s - %i' % (self._players[i].name(), self._players[i].score())
            print(message)

        print('\n  %s wins!\n' % winning_player.name())

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