import os
import string
import operator

my_file = os.path.join('/Users/SE/PycharmProjects/python_basics/test_file/pride.txt')


def count_words(filename):
    """     Build and return the dictionary for the given filename    """
    words_dict = dict()
    with open(my_file, 'r') as outfile:
        for line in outfile.readlines():
            for word in line.split():
                word = word.translate(None, string.punctuation + string.digits).lower()
                if len(word) < 1:
                    continue
                else:
                    words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


def report(word_dict):
    longest_word = max(sorted(word_dict), key=len)
    print "The longest word is: %s" % longest_word
    most_common = sorted(word_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]
    print 'The 5 most common words are: '
    for item in most_common:
        print str(item[0]) + ': ' + str(item[1])

    with open('out.txt', 'w') as outfile:
        for key in sorted(word_dict.iterkeys()):
            outfile.write(str(key) + ": " + str(word_dict[key]) + '\n\n')


def main():
    word_count = count_words(my_file)
    print report(word_count)


if __name__ == '__main__':
    main()
