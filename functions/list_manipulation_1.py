spam = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(my_list):

    string = str()
    for item in range(len(my_list)-1):
        string += str(my_list[item]) + ', '
    return string + "and " + str(my_list[-1])


print list_to_string(spam)
