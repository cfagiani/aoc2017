from days.util import util
import operator


def part1(input_file, output_file=None):
    pipe_map = util.read_input(input_file, tokenizer)
    letters = []
    pos = (0, pipe_map[0].index('|'))
    direction = (1, 0)
    while True:
        pos, direction, took_step = take_step(pos, direction, pipe_map, letters)
        if not took_step:
            break
    print("Letters encountered: {letters}".format(letters=''.join(letters)))


def part2(input_file, output_file=None):
    pipe_map = util.read_input(input_file, tokenizer)
    letters = []
    pos = (0, pipe_map[0].index('|'))
    direction = (1, 0)
    count = 0
    while True:
        pos, direction, took_step = take_step(pos, direction, pipe_map, letters)
        if not took_step:
            break
        count += 1
    print("Took {steps} steps".format(steps=count))


def take_step(pos, direction, pipe_map, letters):
    if not is_valid(pos, pipe_map):
        return pos, direction, False

    if is_straight(pos, pipe_map):
        pos = add(pos, direction)
    elif pipe_map[pos[0]][pos[1]] == '+':
        # only change directions if we can't continue straight
        temp_pos = add(pos, direction)
        if is_valid(temp_pos, pipe_map) and is_straight(temp_pos, pipe_map):
            pos = temp_pos
        else:
            # couldn't go straight, need to turn
            direction = (direction[1], direction[0])
            temp_pos = add(pos, direction)
            if is_valid(temp_pos, pipe_map) and is_straight(temp_pos, pipe_map):
                pos = temp_pos
            else:
                direction = (-direction[0], -direction[1])
                temp_pos = add(pos, direction)
                if is_valid(temp_pos, pipe_map) and is_straight(temp_pos, pipe_map):
                    pos = temp_pos
    elif pipe_map[pos[0]][pos[1]] != ' ':
        # must be a letter
        letters.append(pipe_map[pos[0]][pos[1]])
        pos = add(pos, direction)
    else:
        return pos, direction, False
    return pos, direction, True


def add(a, b):
    return tuple(map(operator.add, a, b))


def is_straight(pos, pipe_map):
    return pipe_map[pos[0]][pos[1]] == '|' or pipe_map[pos[0]][pos[1]] == '-'


def is_valid(pos, pipe_map):
    if pos[0] < 0 or pos[0] >= len(pipe_map):
        return False
    if pos[1] < 0 or pos[1] >= len(pipe_map[pos[0]]):
        return False
    return True


def tokenizer(input):
    return util.line_tok(input, False)
