#!/usr/bin/env python2.6
import sys

def adder(init, adds):
    sum = init
    for addend in adds:	
        sum += addend
    return sum

def main(argv):
    if len(argv) < 2:
        argv.append(0)
    
    print adder(argv[1], argv[2:])
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))