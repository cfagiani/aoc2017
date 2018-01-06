from days.util import util


def part1(input_file, output_file=None):
    instructions = to_ints(util.read_input(input_file, util.line_tok))
    cur_pos = 0
    jump_count = 0
    while 0 <= cur_pos < len(instructions):
        jump = instructions[cur_pos]
        instructions[cur_pos] += 1
        cur_pos += jump
        jump_count += 1
    print "Took {cnt} jumps to exit list".format(cnt=jump_count)


def part2(input_file, output_file=None):
    instructions = to_ints(util.read_input(input_file, util.line_tok))
    cur_pos = 0
    jump_count = 0
    while 0 <= cur_pos < len(instructions):
        jump = instructions[cur_pos]
        if jump >= 3:
            instructions[cur_pos] -= 1
        else:
            instructions[cur_pos] += 1
        cur_pos += jump
        jump_count += 1
    print "Took {cnt} jumps to exit list".format(cnt=jump_count)


def to_ints(data):
    return [int(i) for i in data]
