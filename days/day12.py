from days.util import util


def part1(input_file, output_file=None):
    nodes = build_graph(input_file)

    group = build_group("0", nodes, [])
    print("Node 0 has {cnt} nodes in its group".format(cnt=len(group)))


def part2(input_file, output_file=None):
    nodes = build_graph(input_file)

    groups = []
    total_seen = []
    for node in nodes.values():
        if node.get_id() not in total_seen:
            group = build_group(node.get_id(), nodes, [])
            groups.append(group)
            total_seen += group

    print("There are {cnt} groups".format(cnt=len(groups)))


def build_graph(input_file):
    lines = util.read_input(input_file, util.line_tok)
    nodes = {}
    for line in lines:
        parts = line.split("<->")
        nid = parts[0].strip()
        node = nodes.get(nid, Node(nid))
        nodes[nid] = node
        if len(parts) > 1 and len(parts[1].strip()) > 0:
            for p in parts[1].strip().split(","):
                xid = p.strip()
                if len(xid) > 0:
                    node.connect(xid, nodes)
                    neighbor_node = nodes.get(xid, Node(xid))
    return nodes


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

        # connect dest to self
        peer = nodes.get(oid, Node(oid))
        nodes[oid] = peer
        # connect self to dest
        self.neighbors.append(oid)

    def neighbor_count(self):
        return len(self.neighbors)

    def get_neighbors(self):
        return self.neighbors

    def print_node(self):
        print self.id
        print self.neighbors

    def get_id(self):
        return self.id
