import re


def consonant(abc):

    consonant_regex = re.compile(r'[^aeiouAEIOU]')
    result = consonant_regex.findall(abc)
    return result

request = raw_input("Please Provide text: ")

if len(request) < 1:
    print "Text is not provided"

else:
    if len(consonant(request)) < 1:
        print "There is no consonant"
    else:
        print consonant(request)
