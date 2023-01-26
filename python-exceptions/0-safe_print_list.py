#!/usr/bin/python3
def safe_print_list(my_list, x):
    cnt = 0
    try:
        for i in my_list:
            if ((cnt >= x) or (x == 0)):
                break
            print("{}".format(i), end="")
            cnt += 1
    except NameError:
        print("{:d}".format(my_list))
    finally:
        print()
        return cnt
