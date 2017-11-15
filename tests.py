import unittest

from password_strength import *


class PasswordStrengthTestCase(unittest.TestCase):

    def setUp(self):
        map_of_undesired_words_paths = {'names': './blacklist/names.txt',
                                    'surnames': './blacklist/surnames.txt',
                                    'english words': './blacklist/words.txt'}

        map_of_stop_list_path = {'popular 10000 passwords': './blacklist/popular10000pass.txt',
                             'keyboard combination': './blacklist/keyboard_comb.txt'}

        self.undesired_word_map = load_word_map_using_path_map(map_of_undesired_words_paths)
        self.stop_list_map = load_word_map_using_path_map(map_of_stop_list_path)

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
