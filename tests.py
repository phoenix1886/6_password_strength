import unittest

from password_strength import is_in_blacklist
from password_strength import contains_words
from password_strength import variety_of_symbols
from password_strength import get_password_strength


class PasswordStrengthTestCase(unittest.TestCase):

    def setUp(self):
        self.words_list_dict = {'names': './blacklist/names.txt',
                                'surnames': './blacklist/surnames.txt',
                                'words': './blacklist/words.txt'}

    def test_is_in_blacklist(self):
        self.assertTrue(is_in_blacklist('12345'))
        self.assertFalse(is_in_blacklist('afFgsS123131'))

    def test_contains_words(self):

        self.assertTrue(
            contains_words('George3345', self.words_list_dict['names']))
        self.assertFalse(
            contains_words('!234asdsgd', self.words_list_dict['names']))

        self.assertTrue(
            contains_words('Bush1234', self.words_list_dict['surnames']))
        self.assertFalse(
            contains_words('adssf9g23', self.words_list_dict['surnames']))

        self.assertTrue(
            contains_words('@apple123', self.words_list_dict['words']))
        self.assertFalse(
            contains_words('a!dgdD123', self.words_list_dict['words']))

    def test_varienty_of_symbols(self):
        self.assertEqual(variety_of_symbols('password', 0.25))
        self.assertEqual(variety_of_symbols('Password', 0.5))
        self.assertEqual(variety_of_symbols('Password123', 0.75))
        self.assertEqual(variety_of_symbols('Password123!@++', 1))

    def test_get_password_strength(self):
        self.assertEqual(get_password_strength('1asdgjHHm9++!2dd', 10))
        self.assertEqual(get_password_strength('password1', 1))
        self.assertEqual(get_password_strength('George12!!34241+', 0.75))
        self.assertEqual(get_password_strength('ElenaBielinski123!!!', 0.5))
        self.assertEqual(get_password_strength('Ak1!l5', 0.5))

if __name__ == '__main__':
    unittest.main
