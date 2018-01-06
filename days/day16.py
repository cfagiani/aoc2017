from days.util import util


def part1(input_file, output_file=None):
    moves = util.read_input(input_file)
    positions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for move in moves:
        positions = apply_move(positions, move)
    print ("Final order is {pos}".format(pos=''.join(positions)))


def part2(input_file, output_file=None):
    moves = util.read_input(input_file)
    positions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    seen = [positions[:]]
    while True:
        for move in moves:
            positions = apply_move(positions, move)
        if positions in seen:
            positions = seen[1000000000 % len(seen)]
            break
        else:
            seen.append(positions[:])
    print ("Final order is {pos}".format(pos=''.join(positions)))


def apply_move(pos, move):
    if move.startswith('s'):
        return spin(pos, int(move[1:]))
    elif move.startswith('x'):
        parts = move[1:].split('/')
        return exchange(pos, int(parts[0]), int(parts[1]))
    elif move.startswith('p'):
        parts = move[1:].split('/')
        return partner(pos, parts[0], parts[1])


def spin(pos, spaces):
    end = pos[len(pos) - spaces:]
    start = pos[:len(pos) - spaces]
    return end + start


def exchange(pos, a, b):
    temp = pos[a]
    pos[a] = pos[b]
    pos[b] = temp
    return pos


def partner(pos, a, b):
    return exchange(pos, pos.index(a), pos.index(b))
