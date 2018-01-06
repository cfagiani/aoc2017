from days.util import util
import re


def part1(input_file, output_file=None):
    state_machine, steps = state_machine_builder(input_file)
    tape = {}
    next_pos = 0
    for i in range(steps):
        next_pos = state_machine.take_step(tape, next_pos)
    print("Checksum {cnt}".format(cnt=len(tape)))


def state_machine_builder(input_file):
    lines = util.read_input(input_file, util.line_tok)
    start_state = re.match(r"Begin in state (?P<start_state>[A-Z])", lines[0]).group("start_state")
    steps = re.match(r"Perform a diagnostic checksum after (?P<steps>[0-9]+) steps", lines[1]).group("steps")

    state_machine = StateMachine(start_state)

    i = 2
    while i < len(lines):
        state_def = re.match(r"In state (?P<state_name>[A-Z]):", lines[i])
        if state_def:
            state_machine.add_state(state_def.group("state_name"), lines[i + 1:i + 9])
            i += 9
        else:
            i += 1
    return state_machine, int(steps)


class StateMachine(object):
    def __init__(self, start_state):
        self.cur_state = start_state
        self.states = {}

    def add_state(self, name, config):
        self.states[name] = State(name, config)

    def take_step(self, tape, pos):
        self.cur_state, next_pos = self.states[self.cur_state].apply_production(tape, pos)
        return next_pos


class State(object):
    def __init__(self, name, config):
        self.name, = name
        self.productions = [Production(config[:4]), Production(config[4:])]

    def apply_production(self, tape, pos):
        for p in self.productions:
            if p.is_applicable(tape.get(pos, 0)):
                return p.apply(tape, pos)


class Production(object):
    def __init__(self, config):
        self.condition = int(re.match(r"If the current value is (?P<val>[0-1])", config[0]).group("val"))
        self.to_write = int(re.match(r"- Write the value (?P<val>[0-1])", config[1]).group("val"))
        if re.match(r"- Move one slot to the right", config[2]):
            self.idx_offset = 1
        else:
            self.idx_offset = -1
        self.next_state = re.match(r"- Continue with state (?P<next_state>[A-Z])", config[3]).group("next_state")

    def is_applicable(self, val):
        return val == self.condition

    def apply(self, tape, pos):
        if (self.to_write != 0):
            tape[pos] = self.to_write
        elif tape.get(pos):
            tape.pop(pos)
        return self.next_state, pos + self.idx_offset
