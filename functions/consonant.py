import re


def consonant(string):
    consonant_regex = re.compile(r'[^aeiouAEIOU]')
    result = consonant_regex.findall(string)
    return result


def count_consonant(s):
    consonant_dict = {}
    for letter in consonant(s):
        consonant_dict[letter] = consonant_dict.get(letter, 0) + 1
    return consonant_dict


def print_list(s):
    nice_string = ' '.join(s)
    return nice_string


def print_dict(s):
    for k, v in count_consonant(s).iteritems():
        print k, v


def main():
    user_input = raw_input("Please Provide text: ")
    if len(user_input) < 1:
        print "Text is not provided."
    else:
        if len(consonant(user_input)) < 1:
            print "There is no consonant."
        else:
            print 'Consonant found: %s' % print_list(consonant(user_input))
            print_dict(user_input)


if __name__ == '__main__':
    main()

