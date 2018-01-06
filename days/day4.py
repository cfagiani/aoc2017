from days.util import util
from collections import Counter
from itertools import permutations


def part1(input_file, output=None):
    lines = util.read_input(input_file, util.line_tok)
    valid_phrases = []
    for line in lines:
        if not has_dupe(line):
            valid_phrases.append(line)
    print "There are {n} valid phrases".format(n=len(valid_phrases))


def part2(input_file, output=None):
    lines = util.read_input(input_file, util.line_tok)
    valid_phrases = []
    for line in lines:
        if not has_dupe(line) and not has_anagram(line):
            valid_phrases.append(line)
    print "There are {n} valid phrases".format(n=len(valid_phrases))


def has_anagram(phrase):
    parts = phrase.split()
    for p in parts:
        for perm in permutations(list(p)):
            val = ''.join(perm)
            if p != val and val in parts:
                return True
    return False


def has_dupe(phrase):
    parts = phrase.split()
    c = Counter(parts)
    for p in parts:
        if c.get(p) > 1:
            return True
    return False
