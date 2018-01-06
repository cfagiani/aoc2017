import math


def csv_tok(input, remove_whitespace=True):
    """
    Tokenizes a string by splitting on commas. If remove_whitespace is true, each token will
    have all instances of \n removed before returning as well as being stripped of enclosing whitespace.
    """
    if remove_whitespace:
        return [i.replace('\n', '').strip() for i in input.split(',')]
    else:
        return input.split(',')


def rowwise_space_tok(input, remove_whitespace=True):
    """
    Tokenizes a string by splitting on spaces. If remove_whitespace is true, each token will
    have all instances of \n removed before returning as well as being stripped of enclosing whitespace.
    """
    lines = line_tok(input, remove_whitespace)
    rows = []
    for row in lines:
        rows.append(row.split())
    return rows


def line_tok(input, remove_whitespace=True):
    """Tokenizes a string by splitting on lines. If remove_whitespace is true, each token will be stripped of leading
    and trailing whitespace"""
    if remove_whitespace:
        return [i.strip() for i in input.split("\n")]
    else:
        return input.split("\n")


def read_input(filename, tokenizer=csv_tok):
    """
    Reads an input file and returns a list of tokens (based on the tokenizer provider).
    Tokenizer implementations are assumed to take a single argument (a string containing the full
    text of the file)
    """
    with open(filename, 'r') as infile:
        return tokenizer(infile.read())


def write_file(filename, data):
    """
    Writes the lines in the data list to a file (overwriting if the file exists). Each entry in the list is written
    as a new line (terminated with \n)
    :param filename:
    :param data:
    :return:
    """
    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(data))


def build_2D_array(h, w, init_state=0):
    """
    Builds an array of arrays of the specificed size. All initialized with the init_state
    """
    board = []
    for i in range(0, h):
        board.append([init_state for j in range(w)])
    return board


def rotate_list(list, shift):
    """
    Returns a new list after shifting all members of list to the right (if shift is positive) or left (if negative)
    :param list:
    :param pos_shift:
    :return:
    """
    return list[-shift:] + list[:-shift]


def find_matches(seq, matcher, find_first=False):
    """Searches the seq for items for which the matcher evaluates to True. If find_first is true, a single item
    (or None) will be returned otherwise a list of matches will be returned"""
    results = []
    search_stream = flatten(seq)
    for item in search_stream:
        if matcher(item):
            if find_first:
                return item
            else:
                results.append(item)
    if find_first:
        return None
    else:
        return results


def flatten(seq, intermediate_result=None):
    """
    Recursively flattens a sequence into a single list
    :param seq:
    :param intermediate_result:
    :return:
    """
    if intermediate_result is None:
        intermediate_result = []
    for item in seq:
        if hasattr(item, '__iter__'):
            flatten(item, intermediate_result)
        else:
            intermediate_result.append(item)
    return intermediate_result


def isPrime(num):
    """
    Returns true if a number is prime.
    :param num:
    :return:
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def add_tuples(a, b):
    """
    Pairwise addition of tuples
    :param a:
    :param b:
    :return:
    """
    return tuple(map(sum, zip(a, b)))


def convert_all(data, converter):
    """Converts all entries in a list using the converter function"""
    return [converter(i) for i in data]
