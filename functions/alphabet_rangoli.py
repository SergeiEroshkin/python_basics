import string


def print_rangoli(size):
    alpha = string.ascii_lowercase
    my_list = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        my_list.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(my_list[:0:-1] + my_list))

print_rangoli(5)