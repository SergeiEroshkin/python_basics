def get_value(string, substring):
    # Does not count overlap
    return string.count(substring)


def get_overlap(string, substring):
    count = 0
    for item in range(len(string)):
        if string[item: item + len(substring)] == substring:
            count += 1
    return count


print get_value("oooooo", "ooo")
print get_overlap("oooooo", "ooo")
