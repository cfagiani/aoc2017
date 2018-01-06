import math
from itertools import count


def part1(input_file=None, output_file=None):
    target = 277678

    # diagonal starting one to the right of 1 are all powers of 2 apart so find closest one to target
    side = side_length(target)
    dist_to_center = (side - 1) / 2
    a = [side ** 2 - ((side - 1) * i) - math.floor(side / 2) for i in range(0, 4)]
    steps_to_a = min([abs(axis - target) for axis in a])
    print dist_to_center + steps_to_a


def part2(input_file=None, output_file=None):
    target = 277678
    for x in sum_spiral():
        if x > target:
            print x
            return


def side_length(number):
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side


def sum_spiral():
    a, i, j = {(0, 0): 1}, 0, 0
    sn = lambda i, j: sum(a.get((k, l), 0) for k in range(i - 1, i + 2)
                          for l in range(j - 1, j + 2))
    for s in count(1, 2):
        for _ in range(s):   i += 1; a[i, j] = sn(i, j); yield a[i, j]
        for _ in range(s):   j -= 1; a[i, j] = sn(i, j); yield a[i, j]
        for _ in range(s + 1): i -= 1; a[i, j] = sn(i, j); yield a[i, j]
        for _ in range(s + 1): j += 1; a[i, j] = sn(i, j); yield a[i, j]
