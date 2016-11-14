spam = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(a):

    string = ''
    for item in range((len(a)) - 1):
         string += a[item] + ',' + ' '
    return string + "and" + " " + a[(len(a))-1]

print list_to_string(spam)
