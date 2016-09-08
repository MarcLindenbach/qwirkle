import copy
from player import Player
from game_board import InvalidPlayException


class SingleGreedyBot(Player):
    def play_turn(self, board):
        valid_starts = board.valid_plays()

        plays = []
        for (x, y) in valid_starts:
            tiles = self._tiles.copy()

            for i in range(len(tiles)):
                try:
                    board.play(tiles[i], x=x, y=y)
                    plays.append({
                        'plays': [(x, y, tiles[i])],
                        'score': board.score()
                    })
                    tiles_remaining = tiles.copy()
                    tiles_remaining.pop(i)
                    break
                except InvalidPlayException:
                    pass

            board.reset_turn()

        if len(plays) == 0:
            return

        best_play = max(plays, key=lambda p: p['score'])

        for (x, y, tile) in best_play['plays']:
            board.play(tile, x, y)
            self._tiles.pop(self._tiles.index(tile))
