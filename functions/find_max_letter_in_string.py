def find_max_letter(string):
    """
    Function to get max letter[s] in string.
    :param string: Input string
    :return: Max letter in string
    """
    if len(s) == 0:
        print "The string is empty"
        return
    count_letters = {}
    for letter in string:
        count_letters[letter] = count_letters.get(letter, 0) + 1
    max_letter = max(count_letters.itervalues())
    for key, value in count_letters.iteritems():
        if value == max_letter:
            print key, value

s = "aaabbbbccccddd"
find_max_letter(s)


