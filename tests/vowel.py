import re


def vowel(abc):

    vowel_regex = re.compile(r'[aeiouAEIOU]')
    result = vowel_regex.findall(abc)
    return result

request = raw_input("Please Provide text: ")

if len(request) < 1:
    print "Text is not provided"

else:
    print vowel(request)
