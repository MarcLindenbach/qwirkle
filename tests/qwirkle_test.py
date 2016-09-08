from unittest import TestCase
from qwirkle import QwirkleGame


class QwirkleGameTest(TestCase):

    def test_generate_new_bag_of_tiles_generates_the_correct_amount(self):
        game = QwirkleGame()
        game._generate_new_bag_of_tiles()

        self.assertEqual(108, len(game._bag_of_tiles))
