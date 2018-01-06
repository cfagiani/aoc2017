from days.util import util
import copy


def part1(input_file, output_file=None):
    cur_data = process_data(input_file, 5)
    count = count_pixels(cur_data)
    print("There are {count} pixels on".format(count=count))


def part2(input_file, output_file=None):
    cur_data = process_data(input_file, 18)
    count = count_pixels(cur_data)
    print("There are {count} pixels on".format(count=count))


def count_pixels(cur_data):
    count = 0
    for line in cur_data:
        for c in line:
            if c == '#':
                count += 1
    return count


def process_data(input_file, iterations):
    rules = util.read_input(input_file, rule_tok)
    cur_data = [['.', '#', '.'],
                ['.', '.', '#'],
                ['#', '#', '#']
                ]

    for i in range(iterations):
        print i
        dim = 3
        if len(cur_data) % 2 == 0:
            dim = 2
        squares = []
        for sq in get_squares(cur_data, dim):
            squares.append(translate(sq, rules))
        cur_data = merge_squares(squares)
    return cur_data


def translate(sq, rules):
    for r in rules:
        if r.matches(sq.get_data()):
            return Square(r.get_to(), sq.get_pos())
    raise ValueError("Could not find match")


def merge_squares(squares):
    dim = len(squares[0].get_data())
    max_row = max(squares, key=lambda s: s.get_y()).get_y()
    rows = [[] for i in range((max_row + 1) * dim)]
    row_sorted = sorted(squares, key=lambda x: x.get_y())

    for row_num in range(len(rows)):
        cur_row = sorted(filter(lambda x: x.get_y() == row_num, row_sorted), key=lambda x: x.get_x())
        for sq in cur_row:
            for i in range(dim):
                rows[row_num * dim + i] += sq.get_row(i)
        row_num += 1
    return rows


def get_squares(data, dim):
    squares = []
    for x in range(0, len(data), dim):
        for y in range(0, len(data), dim):
            temp = []
            for j in range(0, dim):
                temp.append(data[y + j][x:x + dim])
            squares.append(Square(temp, (x / dim, y / dim)))
    return squares


def rule_tok(input):
    lines = util.line_tok(input, True)
    rules = []
    for line in lines:
        rules.append(Rule(line))
    return rules


class Rule(object):
    def __init__(self, definition):
        rule_sides = [i.strip() for i in definition.split("=>")]
        self.from_sq = []
        sq = build_square_data(rule_sides[0])
        for i in range(4):
            temp = rotate_sq(sq, i)
            self.from_sq.append(temp)
            self.from_sq.append(flip_sq_x(temp))
            self.from_sq.append(flip_sq_y(temp))

        self.to_sq = build_square_data(rule_sides[1])

    def matches(self, sq):
        if len(sq) != len(self.from_sq[0]):
            return False
        for my_sq in self.from_sq:
            if my_sq == sq:
                return True
        return False

    def get_to(self):
        return self.to_sq


def flip_sq_y(sq):
    mat = copy.deepcopy(sq)
    temp = mat[0]
    mat[0] = mat[len(mat) - 1]
    mat[len(mat) - 1] = temp
    return mat


def flip_sq_x(sq):
    mat = copy.deepcopy(sq)

    for i in range(len(sq)):
        temp = mat[i][0]
        mat[i][0] = mat[i][len(mat) - 1]
        mat[i][len(mat) - 1] = temp
    return mat


def rotate_sq(sq, idx):
    """"rotate sq 90 deg* idx"""

    if idx == 0:
        return sq
    mat = copy.deepcopy(sq)
    for i in range(idx):
        for x in range(len(mat)):
            for y in range(x, len(mat) - x - 1):
                temp = mat[x][y]
                mat[x][y] = mat[y][len(mat) - 1 - x]
                mat[y][len(mat) - 1 - x] = mat[len(mat) - 1 - x][len(mat) - 1 - y]
                mat[len(mat) - 1 - x][len(mat) - 1 - y] = mat[len(mat) - 1 - y][x]
                mat[len(mat) - 1 - y][x] = temp
    return mat


def build_square_data(definition):
    parts = definition.split("/")
    sq = []
    for line in parts:
        sq.append(list(line.strip()))
    return sq


class Square(object):
    def __init__(self, data, pos=None):
        self.pos = pos
        self.data = data

    def get_pos(self):
        return self.pos

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_row(self, row):
        return self.data[row]

    def get_data(self):
        return self.data
