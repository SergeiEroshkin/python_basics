import re


def extract_email(abc):

    email_regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    result = email_regex.findall(abc)
    return result

test_string = open('/Users/SE/PycharmProjects/python_basics/emaillist', 'r')
print extract_email(test_string.read())
