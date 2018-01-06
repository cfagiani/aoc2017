from days.util import util
import operator
import re


def part1(input_file, output_file=None):
    registers = {}
    commands = util.read_input(input_file, util.line_tok)
    for cmd in commands:
        execute_command(cmd, registers)
    max_entry = max(registers.iteritems(), key=operator.itemgetter(1))

    print "Max value is {val} in {reg}".format(val=max_entry[1], reg=max_entry[0])


def part2(input_file, output_file=None):
    registers = {}
    commands = util.read_input(input_file, util.line_tok)
    max_entry = None
    for cmd in commands:
        execute_command(cmd, registers)
        if len(registers) > 0:
            cur_max = max(registers.iteritems(), key=operator.itemgetter(1))
            if max_entry is None:
                max_entry = cur_max
            elif max_entry[1] < cur_max[1]:
                max_entry = cur_max

    print "Max value is {val} in {reg}".format(val=max_entry[1], reg=max_entry[0])


def execute_command(cmd, registers):
    pattern = re.compile(
        r"(?P<dest_reg>[a-z]+) (?P<op>inc|dec) (?P<adj_val>[-]*[0-9]+) if (?P<comp_reg>[a-z]+) (?P<comp_op>==|<|>|<=|>=|!=) (?P<comp_val>[-]*[0-9]+)")
    match = pattern.match(cmd)
    comp_reg_val = registers.get(match.group("comp_reg"), 0)
    if is_true(comp_reg_val, match.group("comp_op"), int(match.group("comp_val"))):
        apply_delta(match.group("dest_reg"), match.group("op"), int(match.group("adj_val")), registers)


def apply_delta(reg, op, adj, registers):
    cur_val = registers.get(reg, 0)
    if op == "inc":
        registers[reg] = cur_val + adj
    else:
        registers[reg] = cur_val - adj


def is_true(val1, op, val2):
    if op == "==":
        return val1 == val2
    elif op == ">=":
        return val1 >= val2
    elif op == "<=":
        return val1 <= val2
    elif op == "<":
        return val1 < val2
    elif op == ">":
        return val1 > val2
    elif op == "!=":
        return val1 != val2

        #
        # if init_pattern.match(line):
        #   commands.append(line)
        # else:
        #    match = cmd_bot_pattern.match(line)
        #   bots[match.group("source_bot")] = Bot(line)
