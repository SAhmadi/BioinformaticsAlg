#!/usr/bin/env python3
# 
# Input:    Text T, Pattern s, int k
# Output:   First occurance of s' in T
#           where hammingDist(s, s') <= k


def hamming_distance(pattern, motiv):
    """ 
    Calculates the Hamming-Distance of pattern and motiv
    """
    if len(pattern) != len(motiv): return -1

    hamming_distance = 0
    for i in range(0, len(motiv)):
        if pattern[i] != motiv[i]:
            hamming_distance += 1
    
    return hamming_distance


def main():
    T = "TTACCTTAACGATATCTGTCACGGCGTTCGCCCTAAAGAGCGTCAGAGGT"
    s = "AAA"
    s_dash = ""
    k = 1

    did_occure = False
    index = -1

    for i in range(len(T)):
        if i + len(s)-1 >= len(T): break

        hd = hamming_distance(s, T[i : i+len(s)])

        if hd == -1: continue
        elif hd <= k:
            s_dash = T[i : i + len(s)]
            did_occure = True
            index = i
            break

    if did_occure:
        print("Index {}, hammDist(s={}, s'={}) = {}".format(index, s, s_dash, hd)) 
    else:
        print("Motiv not found!")


if __name__ == "__main__":
    main()