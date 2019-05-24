#!/usr/bin/env python
# -*- coding: utf-8 -*-:q

import argparse


def tail_main():
    parser = argparse.ArgumentParser(description='argparse sample.')

    # 数値オプション
    parser.add_argument('-n', '--number', type=int, help='data number')
    # 文字列オプション
    parser.add_argument('-f', '--file_path', type=str, help='data file_path')
    # bool オプション
    # parser.add_argument('-r', '--reverse', type=str, default=False,
    # help='Use tail_command => True, Use head_command => False')

    args = parser.parse_args()

    print(args.number)
    print(args.file)
    # print(args.reverse)

    number_of_line_from_end = args.number
    file_path = args.file_path
    is_reverse = args.reverse.title

    # reverse_switch = -1 if is_reverse else 1
    reverse_switch = -1

    def read_file(path):
        with open(path, 'r') as file_contents:
            return file_contents.readlines()

    line_of_contents_list = read_file(file_path)
    result_output = ''.join(
        line_of_contents_list[reverse_switch * int(number_of_line_from_end):])

    print(result_output)
