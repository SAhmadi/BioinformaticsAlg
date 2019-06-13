#!/usr/bin/env python3
#
# Input: Set X
# Output: Multiset of X

def multiSet(s):
    """ 
    Calculate the multiset of s
    """
    if len(s) == 0: return []
    
    multiSet = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            multiSet.append(s[j] - s[i])
    
    return multiSet


def main():
    X = [0, 2, 4, 7, 10]
    delta_X = sorted(multiSet(X))
    print(delta_X)


if __name__ == "__main__":
    main()