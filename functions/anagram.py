def anagram(string1, string2):

    """
    :param string1: Any input string
    :param string2: Any input string
    :return: True or False
    """
    if len(string1) != len(string2):
        return False
    str1_list = list(string1)
    str2_list = list(string2)
    return str1_list.sort() == str2_list.sort()

a = "Hello,World"
b = a[::-1]
c = "Welcome"
print anagram(a, b)
print anagram(a, c)
