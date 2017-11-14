import getpass

from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import digits

PATHS_OF_UNDESIRED_WORDS_TO_USE = {'names': './blacklist/names.txt',
                                   'surnames': './blacklist/surnames.txt',
                                   'english words': './blacklist/words.txt'}

def is_in_stop_list(password):

    path_of_stop_list = './blacklist/popular10000pass.txt'
    try:
        with open(path_of_stop_list) as black_list:
            for word in black_list:
                if password == word.rstrip():
                    return True
            return False
    except FileNotFoundError:
        print('File not found path: {}'.format(path_of_stop_list))


def contains_undesired_words(password, path_of_undesired_words_list):

    password = password.lower()
    try:
        with open(path_of_undesired_words_list) as stop_list:
            for word in stop_list:
                word = word.rstrip().lower()
                min_reasonable_length_of_word = 3
                if len(word) > min_reasonable_length_of_word and \
                                word in password:
                    return True
            return False
    except FileNotFoundError:
        print('File not found path: {}'.format(path_of_undesired_words_list))


def proportion_of_symbol_types_used(password):

    types_of_symbols_map = {'uppercase': ascii_uppercase,
                            'lowercase': ascii_lowercase,
                            'digits': digits,
                            'punctuation': punctuation}
    types_of_symbols_found = 0
    for symbol_types, type_list in types_of_symbols_map.items():
        for char in password:
            if char in type_list:
                types_of_symbols_found += 1
                break

    return types_of_symbols_found / len(types_of_symbols_map)


def get_password_strength(password):

    min_possible_strength_score = 1
    max_possible_strength_score = 10

    if is_in_stop_list(password):
        return min_possible_strength_score

    starting_score = 10
    strength_score = starting_score

    recommended_password_length = 12
    strength_score *= len(password) / recommended_password_length

    strength_score *= proportion_of_symbol_types_used(password)

    for path_of_undesired_word_list in PATHS_OF_UNDESIRED_WORDS_TO_USE.values():
        if contains_undesired_words(password, path_of_undesired_word_list):
            penalty_multiplier = 0.75
            strength_score *= penalty_multiplier

    strength_score = max(strength_score, min_possible_strength_score)
    strength_score = min(strength_score, max_possible_strength_score)

    return strength_score


if __name__ == '__main__':
    password = getpass.getpass(prompt="Type the password to evaluate: ")
    print("The strength of the password: {:.1f}"
          .format(get_password_strength(password)))
