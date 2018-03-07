def find_max_letter(string):
    """
    Function to get max letter in string. If multiple - return first letter.
    :param string: Input string
    :return: Max letter in string
    """
    if len(s) == 0:
        print "The string is empty"
        return False
    count_letters = {}
    for letter in string:
        count_letters[letter] = count_letters.get(letter, 0) + 1
    max_occurrence = max(count_letters.values())
    for k, v in count_letters.iteritems():
        if v == max_occurrence:
            print k

s = "aaabbbbccccddd"
print find_max_letter(s)
