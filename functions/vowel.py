import re


def vowel(abc):

    vowel_regex = re.compile(r'[aeiouAEIOU]')
    result = vowel_regex.findall(abc)
    return result


request = raw_input("Please Provide text: ")

if len(request) < 1:
    print "Text is not provided"

else:
    if len(vowel(request)) < 1:
        print "There is no vowel"
    else:
        print vowel(request)
