from days.util import util

binary_ops = ['set', 'add', 'mul', 'mod', 'jgz', 'sub', 'jnz']


def part1(input_file, output_file=None):
    instructions = util.read_input(input_file, util.line_tok)
    ptr = 0
    process = Process(0)
    mul_count = 0
    while ptr >= 0 and ptr < len(instructions):
        ins = instructions[ptr]
        ptr = process.handle_instruction(ins, [])[0]
        parts = ins.split()
        if parts[0] == 'mul':
            mul_count += 1
    print("Performed {cnt} mul operations".format(cnt=mul_count))


def part2(input_file, output_file):
    translated_program = ["#include <stdio.h>",
                          "int main(int argc, char** argv)",
                          "{",
                          "long a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;"]
    lines = util.read_input(input_file, util.line_tok)
    for num, line in enumerate(lines):
        translated_program.append(translate_line(num, line, len(lines)))
    translated_program += ["eop:", 'printf("%ld\\n", h);', "}"]
    util.write_file(output_file, translated_program)
    print("Manually optimize, then compile and execute {file} for solution".format(file=output_file))


def translate_line(num, line, max_ptr):
    cmd, argx, argy = line.split()
    if cmd == 'jnz':
        if 0 <= num + int(argy) < max_ptr:
            destline = "line{num}".format(num=num + int(argy))
        else:
            destline = "eop"
        translated = "if ({x} != 0) goto {dest};".format(x=argx, dest=destline)
    else:
        op = " = "
        if cmd == 'sub':
            op = " -= "
        elif cmd == 'mul':
            op = " *= "
        translated = "{x}{op}{y};".format(x=argx, op=op, y=argy)

    return "line{num}: {code}".format(num=num, code=translated)


class Process(object):
    def __init__(self, id_num):
        self.registers = {}
        self.buffer = []
        self.id = id_num
        self.registers['a'] = id_num
        self.input_buffer = []
        self.cur_ptr = 0
        self.terminated = False
        self.blocked = False
        self.send_count = 0

    def handle_instruction(self, ins, output_buffer):
        parts = ins.split()
        self.blocked = False
        if parts[0] in binary_ops:
            try:
                val = int(parts[2])
            except ValueError:
                val = self.registers.get(parts[2], 0)
            try:
                valX = int(parts[1])
            except ValueError:
                valX = self.registers.get(parts[1], 0)

            if parts[0] == 'set':
                self.registers[parts[1]] = val
            elif parts[0] == 'add':
                self.registers[parts[1]] = val + valX
            elif parts[0] == 'mul':
                self.registers[parts[1]] = valX * val
            elif parts[0] == 'mod':
                self.registers[parts[1]] = valX % val
            elif parts[0] == 'sub':
                self.registers[parts[1]] = valX - val
            elif parts[0] == 'jnz':
                if valX != 0:
                    self.cur_ptr += val
                    return self.cur_ptr, self.blocked
            elif parts[0] == 'jgz':
                if valX > 0:
                    self.cur_ptr += val
                    return self.cur_ptr, self.blocked
        elif parts[0] == 'snd' or parts[0] == 'rcv':
            try:
                val = int(parts[1])
            except ValueError:
                val = self.registers.get(parts[1], 0)
            if parts[0] == 'snd':
                self.send_count += 1
                output_buffer.append(val)
            elif parts[0] == 'rcv':
                if len(self.input_buffer) > 0:
                    self.registers[parts[1]] = self.input_buffer.pop(0)
                else:
                    self.blocked = True
                    return self.cur_ptr, self.blocked
        self.cur_ptr += 1
        return self.cur_ptr, self.blocked

    def get_val(self, raw_val):
        try:
            return int(raw_val)
        except ValueError:
            return self.registers.get(raw_val, 0)

    def get_buffer(self):
        return self.input_buffer

    def terminate(self):
        self.terminated = True

    def is_terminated(self):
        return self.terminated

    def is_blocked(self):
        return self.blocked

    def check_pointer(self, instructions):
        if self.cur_ptr < 0 or self.cur_ptr >= len(instructions):
            self.terminate()

    def get_ptr(self):
        return self.cur_ptr

    def unblock(self):
        self.blocked = False

    def get_send_count(self):
        return self.send_count

    def get_register(self, reg):
        return self.registers.get(reg, 0)
