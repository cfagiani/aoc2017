from days.util import util


def part1(input_file, output_file=None):
    min_node, nodes = init(input_file)
    print "Root is {name} with level {weight}".format(name=min_node.get_name(), weight=min_node.get_level())


def part2(input_file, output_file=None):
    root, nodes = init(input_file)
    # start with root and walk tree, ensure each node has balance
    check_tree(root.get_name(), nodes)


def init(input_file):
    data = util.read_input(input_file, util.line_tok)
    node_map = {}
    for line in data:
        node = Node(line)
        node_map[node.name] = node

    # now build the tree
    set_levels(node_map)
    min_node = None

    for node in node_map.values():
        if min_node is None:
            min_node = node
        elif min_node.get_level() > node.get_level():
            min_node = node
    return min_node, node_map


def check_tree(root_name, node_map):
    val = None
    out_of_bal = False
    for kid in node_map[root_name].get_children():
        if val is None:
            val = node_map[kid].get_total_weight(node_map)
        else:
            if val != node_map[kid].get_total_weight(node_map):
                out_of_bal = True
                print "Node {node} is unbalanced. Children are:".format(node=root_name)
                for k in node_map[root_name].get_children():
                    print "{name}: {w}".format(name=k, w=node_map[k].get_total_weight(node_map))
    if out_of_bal:
        for kid in node_map[root_name].get_children():
            check_tree(kid, node_map)


def print_tree(root_name, node_map):
    for kid in node_map[root_name].get_children():
        print_tree(kid, node_map)
    print root_name


def set_levels(node_map):
    for node in node_map.values():
        # only nodes with children could possibly be the root
        node.increment_level(node_map, 1)


class Node(object):
    def __init__(self, line):
        parts = line.split()
        self.level = 0
        self.name = parts[0]
        self.weight = 0
        self.weight = int(parts[1].replace("(", "").replace(")", ""))
        self.children_names = []
        if len(parts) > 3:
            for i in range(3, len(parts)):
                self.children_names.append(parts[i].replace(",", ""))

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children_names

    def get_level(self):
        return self.level

    def get_weight(self):
        return self.weight

    def get_total_weight(self, node_map):
        ttl = self.get_weight()
        for k in self.children_names:
            ttl += node_map[k].get_total_weight(node_map)
        return ttl

    def increment_level(self, node_map, step=1):
        self.level += step
        for child_name in self.children_names:
            node_map[child_name].increment_level(node_map, 1)
