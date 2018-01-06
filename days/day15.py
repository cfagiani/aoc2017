factor = [16807, 48271]
start = [512, 191]
criteria = [4,8]
divisor = 2147483647


def part1(input_file=None, output_file=None):
    cur_val = start[:]
    matches = 0
    for i in range(0, 40000000):
        if i % 1000000 == 0:
            print "Iter {i}".format(i=i)
        for j in range(0, 2):
            cur_val[j] = (cur_val[j] * factor[j]) % divisor
        if values_match(cur_val):
            matches += 1
    print "Generators agreed {num} times".format(num=matches)


def part2(input_file=None, output_file=None):
    cur_val = start[:]
    matches = 0
    comparisons = 0
    while comparisons < 5000000:
        if comparisons % 100000 == 0:
            print "Iter {i}".format(i=comparisons)
        for j in range(0, 2):
            done = False
            while not done:
                cur_val[j] = (cur_val[j] * factor[j]) % divisor
                if cur_val[j] % criteria[j] == 0:
                    done = True
        if values_match(cur_val):
            matches += 1
        comparisons += 1
    print "Generators agreed {num} times".format(num=matches)

def values_match(vals, bits=16):
    bin_val = []
    for v in vals:
        bin_val.append(to_bin(v).zfill(bits)[-16:])
    return bin_val[0] == bin_val[1]



def to_bin(num):
    return bin(num).replace('0b', '')
