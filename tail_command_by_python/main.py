# _*_ coding: utf-8 _*_
import sys

args_list = sys.argv
number_of_line_from_end = args_list[1]
file_path = args_list[2]


def tail_main(path):
    with open(path, 'r') as file_contents:
        return file_contents.readlines()


line_of_contents_list = tail_main(file_path)
print("".join(line_of_contents_list[(-1 * int(number_of_line_from_end)):]))
