from days.util import util


def part1(input_file, output_file=None):
    spreadsheet = util.read_input(input_file, util.rowwise_space_tok)
    total = 0
    for row in spreadsheet:
        ints = map(int, row)
        total += max(ints) - min(ints)

    print "Checksum {sum}".format(sum=total)


def part2(input_file, output_file=None):
    spreadsheet = util.read_input(input_file, util.rowwise_space_tok)
    total = 0
    for row in spreadsheet:
        total += get_row_val(map(int, row))
    print "Checksum {sum}".format(sum=total)


def get_row_val(row):
    idx = 0
    while idx < len(row):
        for j in range(0, len(row)):
            if idx != j:
                if row[idx] % row[j] == 0:
                    return row[idx] / row[j]
        idx += 1
