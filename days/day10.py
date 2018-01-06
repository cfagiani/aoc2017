from days.util import util


def part1(input_file, output_file=None):
    instructions = util.read_input(input_file)
    data = range(0, 256)
    cur_pos = 0
    skip_size = 0
    data, cur_pos, skip_size = apply_transform(instructions, data, cur_pos, skip_size)
    print "Product of the first two elements is {prd}".format(prd=(data[0] * data[1]))


def part2(input_file, output_file=None):
    raw_input = util.read_input(input_file, util.line_tok)[0]
    input = []
    for c in raw_input:
        input.append(ord(c))
    input += [17, 31, 73, 47, 23]
    data = range(0, 256)
    cur_pos = 0
    skip_size = 0
    for i in range(0, 64):
        data, cur_pos, skip_size = apply_transform(input, data, cur_pos, skip_size)
    hash_raw = []
    cur_hash = 0
    for i in range(0, len(data)):
        cur_hash = cur_hash ^ data[i]
        if (i + 1) % 16 == 0:
            hash_raw.append(cur_hash)
            cur_hash = 0
    hex_hash = [hex(i).replace("0x", "").zfill(2) for i in hash_raw]
    print "Hash is {hash}".format(hash=''.join(hex_hash))


def apply_transform(instructions, data, cur_pos, skip_size):
    for next_str in instructions:
        next_len = int(next_str)
        if (cur_pos + next_len) < len(data):
            sublist = data[cur_pos:(cur_pos + next_len)]
        else:
            sublist = data[cur_pos:]
        if len(data) < (cur_pos + next_len):
            times = (cur_pos + next_len) / len(data)
            for i in range(0, times):
                sublist += data
            sublist += data[0:(cur_pos + next_len) % len(data)]
        sublist.reverse()
        i = cur_pos
        pos = 0
        while pos < next_len:
            if pos + cur_pos < len(data):
                data[pos + cur_pos] = sublist[pos]
            else:
                data[(pos + cur_pos) % len(data)] = sublist[pos]
            pos += 1

        cur_pos += next_len + skip_size
        skip_size += 1
        if cur_pos > len(data):
            cur_pos = cur_pos - len(data)
    return data, cur_pos, skip_size
