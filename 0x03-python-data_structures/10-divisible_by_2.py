#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for number in my_list:
        new_list.append(number % 2 == 0)
    return new_list
