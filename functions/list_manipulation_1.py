spam = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(my_list):

    string = str()
    for item in range(len(my_list)-1):
        string += '%s, ' % str(my_list[item])
    return string + "and %s" % str(my_list[-1])


print list_to_string(spam)
