def part1(input_file=None, output_file=None):
    hashes = compute_hashes()
    bit_count = 0
    for hash_str in hashes:
        bin_str = bin(int(hash_str, 16))[2:].zfill(128)
        bit_count += bin_str.count("1")
    print "There are {num} used blocks".format(num=bit_count)


def part2(input_file=None, output_file=None):
    hashes = compute_hashes()
    grid = []
    for hash_str in hashes:
        bin_str = bin(int(hash_str, 16))[2:].zfill(128)
        grid.append(list(bin_str))
    nodes = build_nodes(grid)

    groups = count_groups(nodes)
    print("There are {cnt} groups".format(cnt=len(groups)))


def build_nodes(grid):
    nodes = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == '1':
                n = nodes.get((i, j), Node((i, j)))
                nodes[(i, j)] = n

                if i > 0 and grid[i - 1][j] == '1':
                    n.connect((i - 1, j), nodes)

                if i < len(grid) - 1 and grid[i + 1][j] == '1':
                    n.connect((i + 1, j), nodes)

                if j < len(grid) - 1 and grid[i][j + 1] == '1':
                    n.connect((i, j + 1), nodes)

                if j > 0 and grid[i][j - 1] == '1':
                    n.connect((i, j - 1), nodes)
    return nodes


def compute_hashes(num=128):
    hashes = []
    for i in range(0, num):
        row_str = 'ugkiagan-{i}'.format(i=i)
        # row_str = 'flqrgnkx-{i}'.format(i=i) #test input
        hashes.append(compute_hash(row_str))
    return hashes


def compute_hash(raw_input):
    hash_input = []
    for c in raw_input:
        hash_input.append(ord(c))
    hash_input += [17, 31, 73, 47, 23]
    data = range(0, 256)
    cur_pos = 0
    skip_size = 0
    for i in range(0, 64):
        data, cur_pos, skip_size = apply_transform(hash_input, data, cur_pos, skip_size)
    hash_raw = []
    cur_hash = 0
    for i in range(0, len(data)):
        cur_hash = cur_hash ^ data[i]
        if (i + 1) % 16 == 0:
            hash_raw.append(cur_hash)
            cur_hash = 0
    hex_hash = [hex(i).replace("0x", "").zfill(2) for i in hash_raw]
    return ''.join(hex_hash)


def apply_transform(instructions, data, cur_pos, skip_size):
    for next_str in instructions:
        next_len = int(next_str)
        if (cur_pos + next_len) < len(data):
            sublist = data[cur_pos:(cur_pos + next_len)]
        else:
            sublist = data[cur_pos:]
        if len(data) < (cur_pos + next_len):
            times = (cur_pos + next_len) / len(data)
            for i in range(0, times):
                sublist += data
            sublist += data[0:(cur_pos + next_len) % len(data)]
        sublist.reverse()
        pos = 0
        while pos < next_len:
            if pos + cur_pos < len(data):
                data[pos + cur_pos] = sublist[pos]
            else:
                data[(pos + cur_pos) % len(data)] = sublist[pos]
            pos += 1

        cur_pos += next_len + skip_size
        skip_size += 1
        if cur_pos > len(data):
            cur_pos = cur_pos - len(data)
    return data, cur_pos, skip_size


def count_groups(nodes):
    groups = []
    total_seen = []
    for node in nodes.values():
        if node.get_id() not in total_seen:
            group = build_group(node.get_id(), nodes, [])
            groups.append(group)
            total_seen += group

    return groups


def build_group(nid, nodes, group):
    if nid not in group:
        group.append(nid)
    node = nodes[nid]
    for n in node.get_neighbors():
        if n not in group:
            build_group(n, nodes, group)
    return group


class Node(object):
    def __init__(self, nid):
        self.id = nid
        self.neighbors = []

    def connect(self, oid, nodes):
        if oid in self.neighbors:
            return

        # connect self to dest
        self.neighbors.append(oid)

        # connect dest to self
        peer = nodes.get(oid, Node(oid))
        nodes[oid] = peer
        peer.connect(self.id, nodes)

    def neighbor_count(self):
        return len(self.neighbors)

    def get_neighbors(self):
        return self.neighbors

    def get_neighbor_str(self):
        nstr = []
        for n in self.neighbors:
            nstr.append(str(n))
        return ','.join(nstr)

    def print_node(self):
        print self.id
        print self.neighbors

    def get_id(self):
        return self.id
