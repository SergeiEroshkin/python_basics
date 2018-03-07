def is_palindrome(s):
    return s == s[::-1]


test_string1 = 'malayalam'
test_string2 = 'malayalme'
print is_palindrome(test_string1)
print is_palindrome(test_string2)
