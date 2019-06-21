#!/usr/bin/env python3
#
# Input: k-mer x, int d
# Output: d-neighbourhood

allowedLetters = ["A", "C", "G", "T"]

def hamming_distance(pattern, motiv):
    """ 
    Calculates the hamming distance
    between its two parameters
    """
    if len(pattern) != len(motiv):
        return -1

    hamming_distance = 0
    for i in range(len(motiv)):
        if pattern[i] != motiv[i]:
            hamming_distance += 1
    
    return hamming_distance


def d_neighbourhood(s, distance):
    """ 
    Calculates d-neighbourhood of a k-mer s 
    with a Distance d 
    """
    if distance == 0:
        return set([s])
    
    if len(s) == 1:
        return set(["A", "C", "G", "T"])

    neighborhood = set([])
    first, rest = s[0], s[1:]

    rest_neighbors = d_neighbourhood(rest, distance)

    for n in rest_neighbors:
        if hamming_distance(rest, n) < distance:
            for nucl in "ACGT":
                neighborhood = neighborhood.union([nucl + n])
        else:
            neighborhood = neighborhood.union([first + n])  

    return neighborhood


def main():
    x = "ACG"
    d = 2
    print(sorted(d_neighbourhood(x, d)))


if __name__ == "__main__":
    main()