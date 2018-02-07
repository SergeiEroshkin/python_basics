def get_value(string, substring):
    return string.count(substring)


def get_value_loop(string, substring):
    count = 0
    for letter in range(0, len(string)):
        if string[letter:letter + len(substring)] == substring:
            count += 1
    return count


print get_value("lololo lo", "lo")