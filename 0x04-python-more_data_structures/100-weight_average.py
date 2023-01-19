#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_of_products = 0
    sum_of_index_1 = 0
    for elements in my_list:
        sum_of_products += elements[0] * elements[1]
        sum_of_index_1 += elements[1]
    return sum_of_products / sum_of_index_1
