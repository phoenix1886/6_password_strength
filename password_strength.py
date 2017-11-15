import getpass

from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import digits

PATHS_OF_UNDESIRED_WORDS_TO_USE = {'names': './blacklist/names.txt',
                                   'surnames': './blacklist/surnames.txt',
                                   'english words': './blacklist/words.txt'}
PATHS_OF_STOP_LISTS = ['./blacklist/popular10000pass.txt']


def get_word_list_from_file(file_path):

    word_list_for_output = []
    try:
        with open(file_path) as words_list:
            for word in words_list:
                word_list_for_output.append(word.rstrip().lower())
    except FileNotFoundError:
        print('File not found path: {}'.format(file_path))

    return word_list_for_output


def is_in_stop_list(password):

    password = password.lower()
    stop_list = []

    for path in PATHS_OF_STOP_LISTS:
        stop_list.extend(get_word_list_from_file(path))

    for word in stop_list:
        if password == word.rstrip():
            return True
    return False


def contains_undesired_words(password, path_of_undesired_word_list):

    password = password.lower()
    undesired_word_list = get_word_list_from_file(path_of_undesired_word_list)

    for word in undesired_word_list:
        min_reasonable_length_of_word = 3
        if len(word) > min_reasonable_length_of_word and word in password:
            return True
    return False


def get_proportion_of_symbol_types_used(password):

    types_of_symbols_map = {'uppercase': ascii_uppercase,
                            'lowercase': ascii_lowercase,
                            'digits': digits,
                            'punctuation': punctuation}
    types_of_symbols_found = 0
    for symbol_list in types_of_symbols_map.values():
        for char in password:
            if char in symbol_list:
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

    strength_score *= get_proportion_of_symbol_types_used(password)

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
