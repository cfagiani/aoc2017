from days.util import util
from collections import Counter
import operator


def part1(input_file, output_file):
    particles = load_particles(input_file)

    min_accel = None

    for i in range(0, len(particles)):
        p_accel = particles[i].get_abs_accel()
        if min_accel is None:
            min_accel = p_accel
        elif p_accel < min_accel:
            min_accel = p_accel
    min_accels = []
    for i in range(len(particles)):
        if particles[i].get_abs_accel() == min_accel:
            min_accels.append(i)
    min_idx = -1
    min_vel = None
    for i in min_accels:
        p_vel = particles[i].get_dot_prd()
        if min_vel is None:
            min_vel = p_vel
            min_idx = i
        elif p_vel < min_vel:
            min_vel = p_vel
            min_idx = i
    print "Particle {idx} stays closest".format(idx=min_idx)


def part2(input_file, output_file=None):
    particles = load_particles(input_file)
    for i in xrange(10000):
        c = Counter(x.get_pos() for x in particles)
        particles = [x.tick() for x in particles if c[x.get_pos()] == 1]

    print "There are {num} particles left".format(num=len(particles))


def load_particles(input_file):
    input_lines = util.read_input(input_file, util.line_tok)
    particles = []
    for line in input_lines:
        particles.append(Particle(line))
    return particles


class Particle(object):
    def __init__(self, conf):
        nums = [int(p) for p in
                conf.replace('p=<', '').replace('v=<', '').replace('a=<', '').replace('>', '').replace(' ', '').split(
                    ",")]
        self.pos = (nums[0], nums[1], nums[2])
        self.vel = (nums[3], nums[4], nums[5])
        self.acc = (nums[6], nums[7], nums[8])

    def tick(self):
        self.vel = tuple(map(operator.add, self.vel, self.acc))
        self.pos = tuple(map(operator.add, self.pos, self.vel))

        return self

    def get_dist(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])

    def get_dot_prd(self):
        return self.acc[0] * self.vel[0] + self.acc[1] * self.vel[1] + self.acc[2] * self.vel[2]

    def get_abs_accel(self):
        return abs(self.acc[0]) + abs(self.acc[1]) + abs(self.acc[2])

    def get_pos(self):
        return self.pos
