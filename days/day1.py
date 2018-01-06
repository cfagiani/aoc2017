from days.util import util


def part1(input_file, output=None):
    digits = util.read_input(input_file, util.line_tok)[0]
    sum = 0
    for i in range(0, len(digits)):
        if i < len(digits) - 1:
            if digits[i] == digits[i + 1]:
                sum += int(digits[i])
        else:
            if digits[i] == digits[0]:
                sum += int(digits[i])
    print "Sum: {sum}".format(sum=sum)


def part2(input_file, output=None):
    digits = util.read_input(input_file, util.line_tok)[0]
    sum = 0
    step = len(digits) / 2
    for i in range(0, len(digits)):
        if i + step < len(digits):
            if digits[i] == digits[i + step]:
                sum += int(digits[i + step])
        else:
            idx = i + step - len(digits)
            if digits[i] == digits[idx]:
                sum += int(digits[idx])
    print "Sum: {sum}".format(sum=sum)
