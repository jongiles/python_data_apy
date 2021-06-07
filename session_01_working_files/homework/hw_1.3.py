"""
exercise_1.3.py --
FBuilding a set from a file. Write a function collect_unique(filename) that takes a filename argument
and collects a set of unique words from the file (our test will read from sonnet_xv_tiny.txt).
The words must be lowercased and stripped of punctuation before being added to the set.
Finally the function returns a sorted list of these unique words.
Author: Jon Giles
Last Revised: 6/6s/2021
"""
import string

def collect_unique(filename):
    fh = open(filename)
    word_set = set()
    # final_word_list = []

    text = fh.read().split()
    punct = string.punctuation
    for word in text:
        clean_word = word.lower()
        for char in punct:
            clean_word = clean_word.replace(char, "")
        word_set.add(clean_word)
    final_word_list = list(word_set)
    final_word_list.sort()
    return final_word_list

file = "../sonnet_xv_tiny.txt"

print(collect_unique(file))
