import copy
from player import Player
from game_board import InvalidPlayException


class GreedyBot(Player):
    def play_turn(self, board):
        valid_starts = board.valid_plays()

        plays = []
        for (x, y) in valid_starts:
            tiles = self._tiles.copy()

            for i in range(len(tiles)):
                tile_played = False
                try:
                    board.play(tiles[i], x=x, y=y)
                    plays.append({
                        'plays': [(x, y, tiles[i])],
                        'score': board.score()
                    })
                    tiles_remaining = tiles.copy()
                    tiles_remaining.pop(i)
                    tile_played = True
                except InvalidPlayException:
                    pass

                while tile_played:
                    tile_played = False
                    for (nx, ny) in board.valid_plays():
                        for j in range(len(tiles_remaining)):
                            try:
                                board.play(tiles_remaining[j], x=nx, y=ny)
                                plays[-1]['plays'].append((nx, ny, tiles_remaining[j]))
                                plays[-1]['score'] = board.score()
                                tiles_remaining.pop(j)
                                tile_played = True
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
