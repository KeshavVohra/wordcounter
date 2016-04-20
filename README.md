# word-counter
A python word counter, counts words in a file


### Usage ###

    python ./word_counter.py <file_path>


### Tests ###

    python -m unittest -v test


### About ###

#### Matching ####

The following regular expression is used to find a word:

    (?![,.!\'\"*?!;:()-/\\])(\S+)(?<![,.!\'\"*?!;:()-/\\])

The above regular expression matches any sequence of non white space characters excluding any punctuations at the start or end of the word.

Set of punctuations includes : `? ! ' " * : ; ( ) - \ /`

Example
-------
    abc -> abc
    "abc" -> abc
    abc! -> abc
    abc. -> abc
    don't -> don't

#### Counting ####

* Lowercase the input of the file.
* Extract word using the above regular expression.
* Take the length of the list returned by `re.findall`.

#### Top 10 Words ####

* Loop through the words returned by the regular expression and create a dictionary mapping words to the number of time they appear in the list.
* Sort dictionary by value using `sorted` in reverse order.
* Return the first 10 tuples in the sorted list.
