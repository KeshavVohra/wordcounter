#!/usr/bin/python

import sys
import argparse
from os import path

from wordcounter.word_counter import WordCounter


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Outputs the total number of words and the ten most common words in the given file.')
    parser.add_argument("file_path", help='path to the input file.')

    file_path = None
    args = parser.parse_args()
    file_path = args.file_path

    if not path.exists(file_path):
        print "Error: could not find file %s" % file_path
        sys.exit()

    try:
        counter = WordCounter(file_path)
        total = counter.get_total()
        top_ten = counter.get_top(10)
        print "Total words: %d" % total
        print "Top 10 words:"
        for word, count in top_ten:
            print "%s: %d" % (word, count)
    except IOError:
        print "Error: could not read file %s" % file_path
        sys.exit()
