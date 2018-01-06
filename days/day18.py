from days.util import util

binary_ops = ['set', 'add', 'mul', 'mod', 'jgz']


def part1(input_file, output_file=None):
    instructions = util.read_input(input_file, util.line_tok)
    ptr = 0
    process = Process(0)
    sounds = []
    while ptr >= 0 and ptr < len(instructions):
        ins = instructions[ptr]
        ptr = process.handle_instruction(ins, sounds)[0]
        parts = ins.split()
        if parts[0] == 'rcv' and process.get_val(parts[1]) > 0:
            print "Sound val is {snd}".format(snd=sounds[-1])
            break


def part2(input_file, output_file=None):
    instructions = util.read_input(input_file, util.line_tok)
    process0 = Process(0)
    process1 = Process(1)
    block_count = 0
    while True:
        while not process0.is_blocked() and not process0.is_terminated():
            process0.check_pointer(instructions)
            ins = instructions[process0.get_ptr()]
            result = process0.handle_instruction(ins, process1.get_buffer())
            #if result[0] > 1:
             #   block_count = 0

        while not process1.is_blocked() and not process1.is_terminated():
            process1.check_pointer(instructions)
            ins = instructions[process1.get_ptr()]
            result = process1.handle_instruction(ins, process0.get_buffer())
            #if result[0] > 0:
             #   block_count = 0

        if is_done(process0, process1):
            if block_count > 2000:
                break
            else:
                process0.unblock()
                process1.unblock()
                block_count += 1
        else:
            block_count = 0

    print("Program 1 sent a value {cnt} times".format(cnt=process1.get_send_count()))
    #271 too low


def is_done(process0, process1):
    if process0.is_terminated() and process1.is_terminated():
        return True
    elif process0.is_terminated() and process1.is_blocked():
        return True
    elif process0.is_blocked() and process1.is_terminated():
        return True
    elif process0.is_blocked() and process1.is_blocked():
        return True


class Process(object):
    def __init__(self, id_num):
        self.registers = {}
        self.buffer = []
        self.id = id_num
        self.registers['p'] = id_num
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
