#!/usr/bin/env python
# _*_ coding: utf-8 _*_:q

import argparse

parser = argparse.ArgumentParser(description='argparse sample')

# bool option
parser.add_argument('-e', '--error', action='store_true', default=False, help='show error (default: show no error)')

# number option
parser.add_argument('-d', '--data', type=int, help='data number')

# string option
parser.add_argument('-s', '--str', type=str, help='data name')

args = parser.parse_args()

print args

