from days.util import util

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(input_file, output_file=None):
    infected_nodes, pos = read_map(input_file)
    direction = (0, -1)
    inf_count = 0
    for i in xrange(10000):
        caused_infection, direction, pos = perform_burst(infected_nodes, direction, pos)
        if caused_infection:
            inf_count += 1
    print("Caused {cnt} infections".format(cnt=inf_count))


def part2(input_file, output_file=None):
    infected_nodes, pos = read_map(input_file)
    direction = (0, -1)
    inf_count = 0
    for i in xrange(10000000):
        caused_infection, direction, pos = perform_burst_evolved(infected_nodes, direction, pos)
        if caused_infection:
            inf_count += 1
    print("Caused {cnt} infections".format(cnt=inf_count))


def perform_burst_evolved(infected_nodes, direction, pos):
    caused_infection = False
    state = infected_nodes.get(pos, "C")
    if state == "I":
        direction = turn(direction, 1)
        # if we were infected, now we're not
        infected_nodes[pos] = "F"
    elif state == "C":
        direction = turn(direction, -1)
        infected_nodes[pos] = "W"
    elif state == "F":
        direction = turn(direction, 2)
        infected_nodes.pop(pos)
    elif state == "W":
        infected_nodes[pos] = "I"
        caused_infection = True

    pos = tuple(map(sum, zip(pos, direction)))
    return caused_infection, direction, pos


def perform_burst(infected_nodes, direction, pos):
    caused_infection = False
    if infected_nodes.get(pos, "C") == "I":
        direction = turn(direction, 1)
        # if we were infected, now we're not
        infected_nodes.pop(pos)
    else:
        direction = turn(direction, -1)
        infected_nodes[pos] = "I"
        caused_infection = True
    pos = tuple(map(sum, zip(pos, direction)))
    return caused_infection, direction, pos


def turn(direction, step):
    return directions[(directions.index(direction) + step) % len(directions)]


def read_map(input_file):
    infected_nodes = {}

    lines = util.read_input(input_file, util.line_tok)
    line_num = 0
    for line in lines:
        col = 0
        for c in line.strip():
            if c == '#':
                infected_nodes[(col, line_num)] = "I"
            col += 1
        line_num += 1

    return infected_nodes, (col / 2, len(lines) / 2)
