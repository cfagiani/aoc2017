from days.util import util


def part1(input_file, output_file=None):
    stream = util.read_input(input_file, util.line_tok)[0]
    group_count = 0
    group_level = 0
    total_score = 0
    in_ignore = False
    in_garbage = False
    for char in stream:
        if char == "{" and not in_ignore and not in_garbage:
            group_level += 1
        elif char == "}" and not in_ignore and not in_garbage:
            total_score += group_level
            group_level -= 1
            group_count += 1
        elif char == "!" and not in_ignore:
            in_ignore = True
        elif char == "<" and not in_ignore:
            in_garbage = True
        elif char == ">" and not in_ignore:
            in_garbage = False
        elif in_ignore:
            in_ignore = False
    print "Total score of all groups is {score}".format(score=total_score)


def part2(input_file, output_file=None):
    stream = util.read_input(input_file, util.line_tok)[0]
    garbage_chars = 0
    in_ignore = False
    in_garbage = False
    for char in stream:
        if char == "!" and not in_ignore:
            in_ignore = True
        elif char == "<" and not in_ignore and not in_garbage:
            in_garbage = True
        elif char == ">" and not in_ignore:
            in_garbage = False
        elif in_garbage and not in_ignore:
            garbage_chars += 1
        elif in_ignore:
            in_ignore = False
    print "Total garbage chars {ttl}".format(ttl=garbage_chars)
