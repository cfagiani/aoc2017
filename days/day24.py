from days.util import util


def part1(input_file, output_file=None):
    components = get_components(input_file)
    bridges = build_bridges([], components)
    max_sum = find_strongest(bridges)
    print("strongest bridge is {str}".format(str=max_sum))


def part2(input_file, output_file=None):
    components = get_components(input_file)
    bridges = build_bridges([], components)
    max_len = 0
    for b in bridges:
        cur_len = len(b)
        if cur_len > max_len:
            max_len = cur_len

    # now get all the bridges with that length
    longest = [b for b in bridges if len(b) == max_len]
    print("strength of longest bridge is {str}".format(str=find_strongest(longest)))


def find_strongest(bridges):
    max_sum = 0
    for b in bridges:
        cur_sum = get_sum(b)
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


def get_sum(bridge):
    total = 0
    for c in bridge:
        for v in c:
            total += int(v)
    return total


def build_bridges(cur_bridge, components):
    bridges = []
    candidates = find_candidates(cur_bridge, components)
    if len(candidates) == 0:
        # no additional candidates; we're at the end of this bridge
        bridges.append(cur_bridge)
    for c in candidates:
        temp = cur_bridge[:]
        temp.append(c)
        bridges += build_bridges(temp, components)
    return bridges


def get_unused(bridge):
    if len(bridge) == 0:
        return '0'
    if len(bridge) == 1:
        return bridge[0][1]
    else:
        last = bridge[-1]
        prev = bridge[-2]
        for x in last:
            if x not in prev:
                return x
        # if we are here, that means we have a "double" value so just return any one
        return last[0]


def find_candidates(bridge, components):
    val = get_unused(bridge)
    candidates = []
    for c in components:
        if val in c and c not in bridge:
            candidates.append(c)
    return candidates


def get_components(input_file):
    lines = util.read_input(input_file, util.line_tok)
    components = []
    for line in lines:
        components.append(line.split("/"))
    return components


def has_dupes(components):
    vals = {}
    for c in components:
        key = "/".join(sorted(c))
        count = vals.get(key, 0)
        vals[key] = count + 1
    print vals
    for entry in vals.values():
        if entry > 1:
            print True
