#!/usr/bin/python3

import sys


def hamming_distance(a, b):
    """ 
    Calculates the Hamming-Distance of a and b
    """
    if len(a) != len(b):
        print("[Error] Strings need to be of same length!")
        sys.exit(-1)

    hamming_distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hamming_distance += 1
    
    print("Hamming Distance: " + str(hamming_distance))


def main():
    if len(sys.argv) != 3:
        print("[Error] python3 ./hammingDistance.py SEQUENCE1 SEQUENCE2")
        sys.exit(-1)

    hamming_distance(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()