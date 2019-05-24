# _*_ coding: utf-8 _*_
import sys

number_of_line_from_end = sys.argv[1]
file_path = sys.argv[2]


def tail_main(my_path):
    with open(my_path, 'r') as file_contents:
        return file_contents.readlines()


line_of_contents_list = tail_main(file_path)
print("".join(line_of_contents_list[-1 * int(number_of_line_from_end):]))
