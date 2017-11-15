import getpass

from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import digits

from blacklist import load_undesired_word_map
from blacklist import load_stop_list_map


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


def calc_penalty_for_undesired_word_used(password, undesired_word_map):

    password = password.lower()
    penalty = 1
    min_reasonable_word_length = 3
    penalty_for_undesired_word_use = 0.75
    for word_list in undesired_word_map.values():
        for word in word_list:
            if len(word) > min_reasonable_word_length and word in password:
                penalty *= penalty_for_undesired_word_use
                break

    return penalty


def is_in_stop_list_map(password, stop_list_map):

    password = password.lower()
    for stop_list in stop_list_map.values():
        if password in stop_list:
            return True

    return False


def get_password_strength(password, undesired_word_map, stop_list_map):

    min_possible_strength_score = 1
    max_possible_strength_score = 10

    if is_in_stop_list_map(password, stop_list_map):
        return min_possible_strength_score

    strength_score = max_possible_strength_score

    recommended_password_length = 12
    strength_score *= len(password) / recommended_password_length

    strength_score *= calc_penalty_for_symbol_types_used(password)

    strength_score *= calc_penalty_for_undesired_word_used(password, undesired_word_map)

    strength_score = max(strength_score, min_possible_strength_score)
    strength_score = min(strength_score, max_possible_strength_score)

    return strength_score


if __name__ == '__main__':

    undesired_word_map = load_undesired_word_map()
    stop_list_map = load_stop_list_map()

    password = getpass.getpass(prompt="Type the password to evaluate: ")

    password_strength = get_password_strength(
        password, undesired_word_map, stop_list_map)

    print("The strength of the password: {:.1f}"
          .format(password_strength))
