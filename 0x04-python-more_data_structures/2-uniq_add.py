#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_ = 0
    res_list = []
    for item in my_list:
        if item not in res_list:
            res_list.append(item)

    for i in res_list:
        sum_ += i
    return (sum_)
