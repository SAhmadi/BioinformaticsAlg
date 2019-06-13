#!/usr/bin/python3

from random import randint


def main():
    random_num = randint(0, 50)
    total_num_count = 1

    while random_num != 42:
        total_num_count += 1
        print("Random integer: " + str(random_num))
        random_num = randint(0, 50)

    print("Total # of integers: " + str(total_num_count))


if __name__ == "__main__":
    main()