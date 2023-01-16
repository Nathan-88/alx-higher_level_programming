#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_l = []
        for i in range(len(my_list)):
            if i == idx:
                my_list.remove(my_list[i])
        return my_list
