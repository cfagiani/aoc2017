#!/usr/bin/env python

import sys
import argparse
import importlib


def main(opts):
    """
    Determines which Day class to import and run
    :param opts:
    :return:
    """
    try:
        module_name = "days.day" + opts.day
        module = importlib.import_module(module_name)
    except ImportError:
        print "Module {mod} for day not found".format(mod=module_name)
        sys.exit(1)
    method = "part" + opts.part
    print "running {mod}.{method}".format(mod=module_name, method=method)
    executor = getattr(module, method)
    executor(opts.input, opts.output)


def get_cmd_opts(showhelp=False):
    """Builds a command line argument parser and returns the parsed options.
    :param showhelp:
    :return:
    """
    if len(sys.argv) == 1:
        sys.argv.append('--help')

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="Path to output file",
                        metavar="<output_file>")
    parser.add_argument("--input", help="name to input file",
                        metavar="<input_path>")
    parser.add_argument("day", help="Day to run")
    parser.add_argument("part", help="Part to run")
    if showhelp:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


if __name__ == "__main__":
    try:
        main(get_cmd_opts())
    except KeyboardInterrupt as kb:
        print "Caught ctrl+c, exiting..."

else:
    raise RuntimeError("%s is intended as a primary executable, it should not be imported" % (__file__))
