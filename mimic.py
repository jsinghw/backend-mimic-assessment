#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import random
import sys

__author__ = "jsinghw"


def create_mimic_dict(filename):
    with open(filename, 'r') as f:
        word = f.read()
        word = word.replace('\n', ' ').split(' ')
        prev_word = ''
        mimic_dict = {}
        for i in word:
            if prev_word not in mimic_dict.keys():
                mimic_dict[prev_word] = [i]
            elif i != '' and prev_word in mimic_dict.keys():
                if i not in mimic_dict[prev_word]:
                    mimic_dict[prev_word].append(i)
            prev_word = i
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    # uncomment next two lines to print out the entire dict
    # for key in sorted(mimic_dict.keys()):
    #     print('%s: %s' % (key, mimic_dict[key]))

    mimic_txt = ['\n']
    next_word = ''
    for i in range(1, 201):
        if next_word not in mimic_dict.keys():
            start_word = ''
        next_word = random.choice(mimic_dict[start_word])
        if next_word == '':
            next_word = random.choice(mimic_dict[''])
        start_word = next_word
        mimic_txt.append(start_word)
        if i % 25 == 0:
            mimic_txt.append("\n")
    print(' '.join(mimic_txt))


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
