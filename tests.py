import unittest

from password_strength import PATHS_OF_UNDESIRED_WORDS_TO_USE
from password_strength import is_in_stop_list
from password_strength import contains_undesired_words
from password_strength import get_proportion_of_symbol_types_used
from password_strength import get_password_strength


class PasswordStrengthTestCase(unittest.TestCase):

    def test_is_in_stop_list(self):
        self.assertTrue(is_in_stop_list('12345'))
        self.assertFalse(is_in_stop_list('afFgsS123131'))

    def test_contains_undesired_words(self):

        self.assertTrue(
            contains_undesired_words('George3345',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['names']))
        self.assertFalse(
            contains_undesired_words('!234asdsgd',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['names']))

        self.assertTrue(
            contains_undesired_words('Bush1234',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['surnames']))
        self.assertFalse(
            contains_undesired_words('adssf9g23',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['surnames']))

        self.assertTrue(
            contains_undesired_words('@apple123',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['english words']))
        self.assertFalse(
            contains_undesired_words('a!dgdD123',
                                     PATHS_OF_UNDESIRED_WORDS_TO_USE['english words']))

    def test_proportion_of_symbol_types_used(self):
        self.assertEqual(get_proportion_of_symbol_types_used('password'), 0.25)
        self.assertEqual(get_proportion_of_symbol_types_used('Password'), 0.5)
        self.assertEqual(get_proportion_of_symbol_types_used('Password123'), 0.75)
        self.assertEqual(get_proportion_of_symbol_types_used('Password123!@++'), 1)

    def test_get_password_strength(self):
        self.assertEqual(get_password_strength('1asdgjHHm9++!2dd'), 10)
        self.assertEqual(get_password_strength('12345'), 1)


if __name__ == '__main__':
    unittest.main
