#!/usr/bin/python3
def safe_print_list_integers(my_list, x):
    """
    prints the first x elements of a list and only integers.
    """

    cnt = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
        cnt += 1

    print()
    return cnt
