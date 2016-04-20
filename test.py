#!/usr/bin/python

import unittest

from wordcounter.word_counter import WordCounter


class TestWordConter(unittest.TestCase):

    def test_count(self):
        wc = WordCounter("data/file1.txt")

        self.assertEqual(wc.get_total(), 300)

    def test_top_ten(self):
        wc = WordCounter("data/file1.txt")
        top_ten = wc.get_top(10)

        self.assertEqual(len(top_ten), 10)
        self.assertListEqual(top_ten, [('sed', 11), ('quis', 9), ('eu', 8), ('vel', 7), ('elit', 5), ('nunc', 5), ('et', 5), ('leo', 5), ('tortor', 5), ('ultricies', 4)])

    def test_large_file(self):
        wc = WordCounter("data/large_file.txt")

        self.assertEqual(wc.get_total(), 1539000)

    def test_parsing_duplicate_word_with_punctuation(self):
        wc = WordCounter("data/file2.txt")
        top_ten = wc.get_top(10)

        self.assertEqual(wc.get_total(), 10)
        self.assertListEqual(top_ten, [('test', 10)])

    def test_empty_file(self):
        wc = WordCounter("data/empty_file.txt")
        top_ten = wc.get_top(10)

        self.assertEqual(wc.get_total(), 0)
        self.assertListEqual(top_ten, [])

if __name__ == '__main__':
    unittest.main()
