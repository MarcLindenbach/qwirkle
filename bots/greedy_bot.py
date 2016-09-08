from player import Player
from game_board import InvalidPlayException


class GreedyBot(Player):
    def play_turn(self, board):
        valid_starts = board.valid_plays()
        tiles = self._tiles.copy()

        plays = []
        for (x, y) in valid_starts:
            tiles = self._tiles.copy()

            tile_played = False
            for i in range(len(tiles)):
                try:
                    board.play(tiles[i], x=x, y=y)
                    tiles.pop(i)
                    tile_played = True
                    break
                except InvalidPlayException:
                    pass

            if tile_played:
                valid_plays = board.valid_plays()
                for (nx, ny) in valid_plays:
                    for i in range(len(tiles)):
                        try:
                            board.play(tiles[i], nx, ny)
                            tiles.pop(i)
                            break
                        except InvalidPlayException:
                            pass
                plays.append({
                    'plays': board.get_plays(),
                    'score': board.score()
                })
                board.reset_turn()

        best_play = max(plays, key=lambda p: p['score'])

        for (x, y, tile) in best_play['plays']:
            board.play(tile, x, y)
            self._tiles.pop(self._tiles.index(tile))

        self._tiles = tiles.copy()
