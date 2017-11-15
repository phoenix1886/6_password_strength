import unittest

from blacklist import load_undesired_word_map
from blacklist import load_stop_list_map

from password_strength import is_in_stop_list_map
from password_strength import calc_penalty_for_undesired_word_used
from password_strength import calc_penalty_for_symbol_types_used
from password_strength import get_password_strength


class PasswordStrengthTestCase(unittest.TestCase):

    def setUp(self):

        self.undesired_word_map = load_undesired_word_map()
        self.stop_list_map = load_stop_list_map()

    def test_is_in_stop_list_map(self):

        self.assertTrue(is_in_stop_list_map('12345', self.stop_list_map))
        self.assertFalse(is_in_stop_list_map('afFgsS123131', self.stop_list_map))

    def test_calc_penalty_for_undesired_word_used(self):

        self.assertEqual(
            calc_penalty_for_undesired_word_used('Abby',
                                     self.undesired_word_map), 0.75)
        self.assertEqual(
            calc_penalty_for_undesired_word_used('!234asdsgd',
                                     self.undesired_word_map), 1)

        self.assertEqual(
            calc_penalty_for_undesired_word_used('Birne',
                                     self.undesired_word_map), 0.75)
        self.assertEqual(
            calc_penalty_for_undesired_word_used('adssf9g23',
                                     self.undesired_word_map), 1)

        self.assertEqual(
            calc_penalty_for_undesired_word_used('@apple123',
                                     self.undesired_word_map), 0.75)
        self.assertEqual(
            calc_penalty_for_undesired_word_used('a!dgdD123',
                                     self.undesired_word_map), 1)

    def test_calc_penalty_for_symbol_types_used(self):
        self.assertEqual(calc_penalty_for_symbol_types_used('password'), 0.25)
        self.assertEqual(calc_penalty_for_symbol_types_used('Password'), 0.5)
        self.assertEqual(calc_penalty_for_symbol_types_used('Password123'), 0.75)
        self.assertEqual(calc_penalty_for_symbol_types_used('Password123!@++'), 1)

    def test_get_password_strength(self):
        self.assertEqual(
            get_password_strength('1asdgjHHm9++!2dd',
                                  self.undesired_word_map ,self.stop_list_map), 10)
        self.assertEqual(
            get_password_strength('12345',
                                  self.undesired_word_map ,self.stop_list_map), 1)


if __name__ == '__main__':
    unittest.main
