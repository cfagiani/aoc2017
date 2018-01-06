This repo contains my solutions to the [2017 Advent of Code](adventofcode.com/2017) in Python 2.

The code is organized such that any day/part can be run via a single driver program. The syntax for running is:

    aoc.py <day> <part> [--input path/to/input/file] [--output path/to/output/file]

The driver will look in the days directory for a file named day<xx>.py (where xx is the day specified on the command line) 
and will run a function called partYY (where YY is the part specified on the command line). If input and/or output is supplied
the value of that argument will be passed into the partYY function. 

