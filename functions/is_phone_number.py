# -----------------------------------------------------------------------------
# Name: phone_number_validator.py
# Purpose: Verification if string matches phone number format
# Date: February 28 2018
# Author: Sergei Eroshkin
# -----------------------------------------------------------------------------


import re


def is_phone_number(user_string):
    # Check if string length less than minimal length of format
    if len(user_string) < 10:
        print '%s not valid phone number.' % user_string
        return False
    # Create Regex pattern object that satisfied following formats '(nnn) - nnn - nnnn' or 'nnnnnnnnnn'
    valid_formats = re.compile(r'^\(\d{3}\)\s\-\s\d{3}\s\-\s\d{4}$|^\d{10}$')
    if valid_formats.match(user_string):
        print '%s is a valid phone number.' % user_string
        return True
    else:
        print '%s not valid phone number.' % user_string
        return False


def main():
    numbers_list = ['(123) - 123 - 1234', '1231231234', '(123) - 1234 - 123a', '123 - 1234 - 1234', '123123123a',
                    '+1(123) - 123 - 1234', '(123)-123-1234', '123 - 123 - 1234', '(a23) - 123 - 1234',
                    '(123) - 123 - 12345', '(123) - 123 - 123!', '(123)  - 123 - 1234', '(123) - 123 - 1234 ',
                    ' (123) - 123 - 1234', '12312312345', '123123123', '1231231234 ', ' 1231231234', '123123123!', '']

    for number in numbers_list:
        is_phone_number(number)


if __name__ == '__main__':
    main()
