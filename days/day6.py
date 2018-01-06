from days.util import util


def part1(input_file, output_file=None):
    count, state = find_first_dupe(input_file)
    print "Duplicate state encountered after {count} steps".format(count=count)


def part2(input_file, output_file=None):
    count, next_alloc = find_first_dupe(input_file)
    target_state = list(next_alloc)
    count = 0
    while True:
        next_alloc = get_next_alloc(next_alloc)
        count += 1
        if next_alloc == target_state:
            print "loop size is {count}".format(count=count)
            return


def find_first_dupe(input_file):
    next_alloc = [int(i) for i in util.read_input(input_file, util.rowwise_space_tok)[0]]
    seen_states = []
    count = 0
    while True:
        next_alloc = get_next_alloc(next_alloc)
        count += 1
        if next_alloc in seen_states:
            return count, next_alloc
        seen_states.append(next_alloc)


def get_next_alloc(banks):
    next_state = list(banks)
    cur_max = max(next_state)
    idx = banks.index(cur_max)
    next_state[idx] = 0
    for i in range(1, cur_max + 1):
        next_state[(idx + i) % len(next_state)] += 1
    return next_state
