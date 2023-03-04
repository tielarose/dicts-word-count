import sys
import string

def tokenize(filename):
    """Takes in a file, returns a list of tokenized words"""

    # Initialize an empty list for the words
    words_list = []

    # Open file
    file = open(filename)
    # Iterate over each line of file
    for line in file:
        # Replace any punctuation with an empty string, make everything lowercase
        line_no_punctuation = line.translate(str.maketrans('', '', string.punctuation)).lower()
        # Remove trailing white space, split into words
        words_list += line_no_punctuation.rstrip().split(" ")

    return words_list


def count_words(words_list):
    """Takes in a list of words, returns a dictionary of word: count"""

    # Initialize an empty dictionary for the words count
    words_count_dict = {}
    # iterate over each word in that list, add into dictionary
    for word in words_list:
        words_count_dict[word] = words_count_dict.get(word, 0) + 1

    return words_count_dict


def print_words(words_count_dict):
    """Takes in a dictionary, prints each key value pairs on a separate line"""
    for word, count in words_count_dict.items():
        print(word, count)


def count_words_in_file(filename):
    """Count words in file."""

    # Tokenize the words in the file
    words_list = tokenize(filename)

    # Count the words
    words_count_dict = count_words(words_list)

    # Print the words
    print_words(words_count_dict)


count_words_in_file(sys.argv[1])
