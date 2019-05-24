#!/usr/bin/env python
# -*- coding: utf-8 -*-:q

import argparse


def tail_main():
    parser = argparse.ArgumentParser(description='argparse sample.')

    # bool オプション
    parser.add_argument('-e', '--error', action='store_true',
                        default=False, help='show error (default: show no error)')
    # 数値 オプション
    parser.add_argument('-n', '--number', type=int, help='data number')
    # 文字列オプション
    parser.add_argument('-f', '--file', type=str, help='data name')

    args = parser.parse_args()

    # print(args.number)
    # print(args.file)

    number_of_line_from_end = args.number
    file_path = args.file

    def read_file(path):
        with open(path, 'r') as file_contents:
            return file_contents.readlines()

    line_of_contents_list = read_file(file_path)
    print("".join(line_of_contents_list[(-1 * int(number_of_line_from_end)):]))
