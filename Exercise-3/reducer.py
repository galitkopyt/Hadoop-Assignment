#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    top_words = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for _, count in group)
            top_words.append((current_word, total_count))
        except ValueError:
            pass

    top_words.sort(key=lambda x: (-x[1], x[0]))

    for word, count in top_words[:3]:
        print('%s%s%d' % (word, separator, count))

if __name__ == "__main__":
    main()


