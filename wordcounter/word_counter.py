#!/usr/bin/python

import sys
import re
import operator


class WordCounter(object):

    pattern = r"(?![,.!\'\"*?!;:()-/\\])(\S+)(?<![,.!\'\"*?!;:()-/\\])"

    def __init__(self, file_path):
        self.file = open(file_path, 'r')
        self.total = 0
        self.words = []

        content = self.file.read().lower()
        words_found = re.findall(WordCounter.pattern, content)
        self.total = len(words_found)

        words_counts = {}
        for w in words_found:
            if w in words_counts:
                words_counts[w] += 1
            else:
                words_counts[w] = 1

        self.words = sorted(words_counts.items(), key=operator.itemgetter(1), reverse=True)

    def get_total(self):
        return self.total

    def get_top(self, num):
        return self.words[:num]
