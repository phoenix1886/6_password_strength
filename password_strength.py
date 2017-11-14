import getpass

from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import digits


def is_in_blacklist(password):

    path_file = './blacklist/popular10000pass.txt'
    try:
        with open(path_file) as black_list:
            for word in black_list:
                if password == word.rstrip():
                    return True
            return False
    except FileNotFoundError:
        print('File not found path:' + path_file)


def contains_words(password, words_list_path):

    password = password.lower()
    try:
        with open(words_list_path) as black_list:
            for word in black_list:
                word = word.rstrip().lower()
                min_length_of_word = 3
                if len(word) > min_length_of_word and word in password:
                    return True
            return False
    except FileNotFoundError:
        print('File not found path:' + words_list_path)


def variety_of_symbols(password, print_details=False):

    types_of_symbols = {'uppercase': ascii_uppercase,
                        'lowercase': ascii_lowercase,
                        'digits': digits,
                        'punctuation': punctuation}
    types_found = 0
    for keys, type_list in types_of_symbols.items():
        for char in password:
            if char in type_list:
                types_found += 1
                break
        else:
            if print_details:
                print('-25% PENALTY: ' + keys + ' symbols not found!!!')

    return types_found / len(types_of_symbols)


def get_password_strength(password, print_details=False):

    word_list_path = {'names': './blacklist/names.txt',
                      'surnames': './blacklist/surnames.txt',
                      'english words': './blacklist/words.txt'}

    if is_in_blacklist(password):
        if print_details:
            print('Your password is in black list!')
        return 1
    starting_score = 10

    recommended_length = 12
    starting_score *= len(password) / recommended_length

    starting_score *= variety_of_symbols(password, print_details)

    if print_details and len(password) < recommended_length:
        print('{:.0f}% PENALTY: minimum 12 charecters length recommended.'
              .format((len(password)/recommended_length - 1)*100), )

    for key, word_path in word_list_path.items():
        if contains_words(password, word_path):
            penalty_multiplier = 0.75
            starting_score *= penalty_multiplier
            if print_details:
                print('-25% PENALTY: password shouldn\'t contain ' + key)

    min_score = 1
    max_score = 10
    starting_score = max(starting_score, min_score)
    starting_score = min(starting_score, max_score)

    return starting_score


if __name__ == '__main__':
    password = getpass.getpass(prompt="Type the password to evaluate:")
    print("The strength of the password: {:.1f}"
          .format(get_password_strength(password, True)))
