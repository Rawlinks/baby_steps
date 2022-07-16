import unittest
from random import seed

from main import what_would_beat, make_a_selection, decide_a_winner

# object inheritance = TestGameLogic is a TestCase and everything else below
class TestGameLogic(unittest.TestCase):

    def test_decide_a_winner(self):
        winner = decide_a_winner('rock', 'scissors')
        self.assertEqual(winner, 1)

        winner = decide_a_winner('rock', 'paper')
        self.assertEqual(winner, 2)

        winner = decide_a_winner('rock', 'rock')
        self.assertEqual(winner, 0)

        winner = decide_a_winner('paper', 'scissors')
        self.assertEqual(winner, 2)

        winner = decide_a_winner('paper', 'paper')
        self.assertEqual(winner, 0)

        winner = decide_a_winner('paper', 'rock')
        self.assertEqual(winner, 1)

        winner = decide_a_winner('scissors', 'scissors')
        self.assertEqual(winner, 0)

        winner = decide_a_winner('scissors', 'paper')
        self.assertEqual(winner, 1)

        winner = decide_a_winner('scissors', 'rock')
        self.assertEqual(winner, 2)



    def test_randomnly_select(self):
        valid_values = ['rock', 'paper', 'scissors']

        seed(0)

        selection = make_a_selection()
        self.assertIn(selection, valid_values)

        selection = make_a_selection()
        self.assertTrue(selection, 'paper')

        selection = make_a_selection()
        self.assertTrue(selection, 'rock')

        selection = make_a_selection()
        self.assertTrue(selection, 'paper')

        selection = make_a_selection()
        self.assertTrue(selection, 'scissors')

    def test_what_beats_selection(self):
        result = what_would_beat('rock')
        self.assertEqual(result, 'paper')

        result = what_would_beat('paper')
        self.assertEqual(result, 'scissors')

        result = what_would_beat('scissors')
        self.assertEqual(result, 'rock')


if __name__ == '__main__':
    unittest.main()