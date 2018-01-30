def anagram(string1, string2):

    """
    :param string1: Any input string
    :param string2: Any input string
    :return: True or False
    """
    if len(string1) != len(string2):
        return False
    else:
        return sorted(list(string1)) == sorted(list(string2))


#Test data#
a = "Hello,World"
b = a[::-1]
c = "World,Helli"
print anagram(a, b)
print anagram(a, c)

