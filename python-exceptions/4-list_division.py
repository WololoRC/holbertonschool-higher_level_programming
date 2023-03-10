#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    """
    divides element by element 2 lists.
    """

    new_list = []
    for i in range(list_lenght):
        new_list.append(0)
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
    return new_list
    ["finally:"]
