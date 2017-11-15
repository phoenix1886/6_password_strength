

def load_undesired_word_map():

    map_of_undesired_words_paths = {'names': './blacklist/names.txt',
                                    'surnames': './blacklist/surnames.txt',
                                    'english words': './blacklist/words.txt'}
    undesired_word_map = load_word_map_using_path_map(map_of_undesired_words_paths)

    return undesired_word_map


def load_stop_list_map():

    map_of_stop_list_path = {'popular 10000 passwords': './blacklist/popular10000pass.txt',
                             'keyboard combination': './blacklist/keyboard_comb.txt'}
    stop_list_map = load_word_map_using_path_map(map_of_stop_list_path)

    return stop_list_map


def load_word_map_using_path_map(path_map):

    word_map = {}
    for name_of_list, path in path_map.items():
        word_map[name_of_list] = load_word_list(path)

    return word_map


def load_word_list(path):

    word_list_for_output = []
    try:
        with open(path) as words_list:
            for word in words_list:
                word_list_for_output.append(word.rstrip().lower())
    except FileNotFoundError:
        raise FileNotFoundError('File: {} not found.'.format(path))

    return word_list_for_output
