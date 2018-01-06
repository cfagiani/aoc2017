from days.util import util


def part1(input_file, output_file=None):
    steps = util.read_input(input_file)
    pos = [0, 0]
    for step in steps:
        pos = take_step(pos, step)

    print "{steps} steps are needed".format(steps=abs(pos[0]) + abs(pos[1]))


def part2(input_file, output_file=None):
    steps = util.read_input(input_file)
    pos = [0, 0]
    max_steps = 0
    for step in steps:
        pos = take_step(pos, step)

        cur_steps = abs(pos[0]) + abs(pos[1])
        if cur_steps > max_steps:
            max_steps = cur_steps

    print "Max steps away was {steps}".format(steps=max_steps)


def take_step(pos, step):
    if step == 'ne':
        pos[0] += .5
        pos[1] += .5
    elif step == 'n':
        pos[1] += 1
    elif step == 'nw':
        pos[0] += -.5
        pos[1] += .5
    elif step == 'sw':
        pos[0] += -.5
        pos[1] += -.5
    elif step == 's':
        pos[1] += -1
    elif step == 'se':
        pos[0] += .5
        pos[1] += -.5
    return pos
