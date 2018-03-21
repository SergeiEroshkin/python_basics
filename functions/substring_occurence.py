def get_value(string, substring):
    # Does not count overlap
    return string.count(substring)


def get_overlap(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i: i + len(substring)] == substring:
            count += 1
    return count


print get_value("oooooo", "oo")
print get_overlap("oooooo", "oo")
