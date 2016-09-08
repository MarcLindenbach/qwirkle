if __name__ == '__main__':
    import argparse
    from qwirkle import QwirkleGame

    parser = argparse.ArgumentParser(description='Qwirkle')
    parser.add_argument('--players', nargs='+')

    game = QwirkleGame()
    game.main(parser.parse_args().players)
