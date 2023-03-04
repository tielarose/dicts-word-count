# Write a program, wordcount.py, that opens a file and counts how many times each space-separated word occurs in that file. Your program should then output each word and the number of times it appears in the file.

"""Count words in file."""


def count_words(filename):
    words_count = {}

    # open file
    file = open(filename)
    # iterate over each line of file
    for line in file:
        # remove trailing white space, split into words
        words_list = line.rstrip().split(" ")

        # iterate over each word in that list, add into dictionary
        for word in words_list:
            words_count[word] = words_count.get(word, 0) + 1

    for word, count in words_count.items():
        print(word, count)


count_words("test.txt")
