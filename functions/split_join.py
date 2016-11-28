def split_join(string):
    string_list = string.split(" ")
    new_string = '-'.join(string_list)
    return new_string

print split_join("hello world")
