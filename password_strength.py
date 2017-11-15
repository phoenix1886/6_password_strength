import getpass

from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import digits


def load_word_list(path):

    word_list_for_output = []
    try:
        with open(path) as words_list:
            for word in words_list:
                word_list_for_output.append(word.rstrip().lower())
    except FileNotFoundError:
        raise FileNotFoundError('File: {} not found.'.format(path))

    return word_list_for_output


def calc_penalty_for_symbol_types_used(password):

    types_of_symbols_map = {'uppercase': ascii_uppercase,
                            'lowercase': ascii_lowercase,
                            'digits': digits,
                            'punctuation': punctuation}
    types_used = 0
    for symbol_list in types_of_symbols_map.values():
        for char in password:
            if char in symbol_list:
                types_used += 1
                break

    return types_used / len(types_of_symbols_map)


def calc_penalty_for_undesired_word_used(password, map_of_word_lists):

    undesired_word_list_names = ['names', 'surnames', 'english words']
    password = password.lower()
    penalty = 1
    min_reasonable_word_length = 3
    penalty_for_undesired_word_use = 0.75
    for name, word_list in map_of_word_lists.items():
        if name in undesired_word_list_names:
            for word in word_list:
                if len(word) > min_reasonable_word_length and word in password:
                    penalty *= penalty_for_undesired_word_use
                    break

    return penalty


def is_in_stop_lists(password, map_of_word_lists):

    stop_list_names = ['pop10000pass', 'keyboard combination']
    password = password.lower()

    for name_of_stop_list, stop_list in map_of_word_lists.items():
        if name_of_stop_list in stop_list_names and password in stop_list:
            return True

    return False


def get_password_strength(password, map_of_word_lists):

    min_possible_strength_score = 1
    max_possible_strength_score = 10

    if is_in_stop_lists(password, map_of_word_lists):
        return min_possible_strength_score

    strength_score = max_possible_strength_score

    recommended_password_length = 12
    strength_score *= len(password) / recommended_password_length

    strength_score *= calc_penalty_for_symbol_types_used(password)

    strength_score *= calc_penalty_for_undesired_word_used(password, map_of_word_lists)

    strength_score = max(strength_score, min_possible_strength_score)
    strength_score = min(strength_score, max_possible_strength_score)

    return strength_score


if __name__ == '__main__':

    file_paths = {'names': './blacklist/names.txt',
                  'surnames': './blacklist/surnames.txt',
                  'english words': './blacklist/words.txt',
                  'pop10000pass': './blacklist/popular10000pass.txt',
                  'keyboard combination': './blacklist/keyboard_comb.txt'}

    map_of_word_lists = {name: load_word_list(path) for name, path in file_paths.items()}

    password = getpass.getpass(prompt="Type the password to evaluate: ")

    password_strength = get_password_strength(
        password, map_of_word_lists)

    print("The strength of the password: {:.1f}"
          .format(password_strength))
