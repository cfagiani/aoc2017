from days.util import util


def part1(input_file, output_file=None):
    fw = build_firewall(input_file)
    cur_psec = 0
    cur_cost = 0
    max_idx = max(fw, key=int)
    for idx in range(1, max_idx+1):
        cur_psec += 1
        cur_cost += get_severity(cur_psec, idx, fw)[0]
    print ("The total severity is {cost}".format(cost=cur_cost))


def part2(input_file, output_file=None):
    fw = build_firewall(input_file)
    start_time = -1
    max_idx = max(fw, key=int)
    done = False
    while not done:
        done = True
        start_time += 1
        cur_psec = start_time
        for i in range(0, max_idx+1):
            if get_severity(cur_psec, i, fw)[1]:
                done = False
                break
            cur_psec += 1

    print ("To avoid detection, leave at {sec}".format(sec=start_time))


def get_severity(cur_psec, cur_idx, fw):
    if cur_idx < 0:
        return 0, False
    cur_depth = fw.get(cur_idx, 0)
    if cur_depth > 0 and cur_psec % (cur_depth - 1) == 0 and ((cur_psec / (cur_depth - 1) % 2) == 0):
        return cur_depth * cur_idx, True
    return 0, False


def build_firewall(input_file):
    data = util.read_input(input_file, util.line_tok)
    fw = {}
    for line in data:
        parts = line.split(":")
        idx = int(parts[0].strip())
        depth = int(parts[1].strip())
        fw[idx] = depth
    return fw
