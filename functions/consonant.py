import re


def consonant(string):
    """
    :param string:
    :return: List of constant letters or 'There is no consonant.'
    """
    consonant_regex = re.compile(r'[^aeiouAEIOU]')
    result = consonant_regex.findall(string)
    return result


user_input = raw_input("Please Provide text: ")

if len(user_input) < 1:
    print "Text is not provided."
else:
    if len(consonant(user_input)) < 1:
        print "There is no consonant."
    else:
        print consonant(user_input)
