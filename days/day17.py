def part1(input_file=None, output_file=None):
    buffer = [0]
    step_size = 355
    cur_pos = 0
    for i in range(1, 2018):
        idx = (cur_pos + step_size) % len(buffer)
        pre = buffer[:idx + 1]
        post = buffer[idx + 1:]
        pre.append(i)
        buffer = pre + post
        cur_pos = idx + 1
    print("Val after 2017 is {val}".format(val=buffer[buffer.index(2017) + 1]))


def part2(input_file=None, output_file=None):
    cur_len = 1
    step_size = 355
    cur_pos = 0
    last_val = 0
    for i in xrange(1, 50000000):
        idx = (cur_pos + step_size) % cur_len
        if idx == 0:
            last_val = i
        cur_pos = idx + 1
        cur_len += 1

    print("Val after 0 is {val}".format(val=last_val))
