#!/usr/bin/python3
def safe_print_list(my_list, x):
    cnt = 0
    try:
        for i in my_list:
            print("{}".format(i), end="")
            cnt += 1
            if (cnt >= x):
                break
    finally:
        print()
        return cnt
