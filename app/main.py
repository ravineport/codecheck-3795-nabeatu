#!/usr/bin/env python3
import re

num_pattern = re.compile("^\d+(\.\d+)?\Z")


def is_num(str_num):
    if num_pattern.match(str_num):
        return True
    else:
        return False


def is_idiot(str_num):
    if int(str_num) % 3 == 0:
        return True
    else:
        return False


def is_stupid(str_num):
    if '3' in str_num:
        return True
    else:
        return False


def judge_nabeatsu(str_num):
    if not is_num(str_num):
        return "invalid"
    elif is_idiot(str_num) and is_stupid(str_num):
        return "dumb"
    elif is_idiot(str_num):
        return "idiot"
    elif is_stupid(str_num):
        return "stupid"
    else:
        return "smart"


def main(argv):
  for v in argv:
    print(judge_nabeatsu(v))
